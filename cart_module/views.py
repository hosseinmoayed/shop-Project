import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
# Create your views here.
from django.urls import reverse

from cart_module.models import Cart, DetailCart
from product_module.models import Product
from django.shortcuts import redirect
import requests
import json

def AddProductToCartView(request):

    if request.user.is_authenticated:
        product_id = int(request.GET.get("product_id"))
        count = request.GET.get("count")

        if count == None:
            count = 1

        if int(count) < 1:
            return JsonResponse({
                "status": "invalid_count",
                'text': "تعداد کالای انتخاب شده نامعتبر می باشد",
                "title": "خطا!",
                'confirmButtonText': "باشه!",
                "icon": "error",

            })

        product = Product.objects.filter(id=product_id,is_active=True , is_delete=False).first()

        if product is not None:

            current_cart , create = Cart.objects.get_or_create(is_paid=False , user_id=request.user.id)
            product_in_cart = current_cart.detailcart_set.filter(product_id=product_id).first()

            if product_in_cart is not None:
                product_in_cart.count += int(count)
                product_in_cart.save()
            else:
                DetailCart.objects.create(product_id=product_id , cart_id=current_cart.id , count=count)

            return JsonResponse({
                "status" : "successful",
                'title':"محصول با موفقیت به سبد خرید اضافه شد",
                'icon':"success"
            })
        else:
            return JsonResponse({
                "status" : "not_found",
                'text' : "کالای مورد نظر یافت نشد",
                "title" : "خطا!",
                'confirmButtonText': "باشه!",
                "icon": "error",


            })
    else:
        return JsonResponse({
                "status" : "not_auth",
                'text' : "برای اضافه کردن محصول به سبد خرید باید وارد حساب کاربری خود شوید",
                "title" : "خطا!",
                "icon":"warning",
                'confirmButtonText' : "ورود به حساب"
            })


@login_required
def RemovecartView(request):
    if request.user.is_authenticated:
        detail_id = request.GET.get("detail_id")
        if detail_id is None:
            return JsonResponse({
                'status' : "detail_id_not_found"
            })

        deleted_count , deleted = DetailCart.objects.filter(id=detail_id , cart__user_id = request.user.id , cart__is_paid=False).delete()
        if deleted_count ==0:
            return JsonResponse({
                "status": "detail_cart_not_found"
            })


        cart:Cart = Cart.objects.prefetch_related("detailcart_set").filter(is_paid=False , user_id=request.user.id).first()
        total = cart.calculate_total_price()



        context = {
            'cart': cart,
            'total': total
        }





        return render(request , 'includes/cart_ajax.html' , context=context)
    return JsonResponse({
        'status' : 'not-auth'
    })


@login_required
def Change_cart_product_count(request):
    detail_id = request.GET.get("detail_id")
    state = request.GET.get("state")
    if detail_id is None or state is None:
        return JsonResponse({
            'status': "detail_id_or_state_not_found"
        })

    detail_cart = DetailCart.objects.filter(id=detail_id, cart__user_id=request.user.id, cart__is_paid=False).first()
    if detail_cart is None:
        return JsonResponse({
            'status' : 'detail_cart_not_found'
        })

    if state == "increase":
        detail_cart.count += 1
        detail_cart.save()
    elif state == "decrease":
        if detail_cart.count == 1:
            detail_cart.delete()
        else:
            detail_cart.count -= 1
            detail_cart.save()
    else:
        return JsonResponse({
            'status': "state_invalid"
        })

    cart: Cart = Cart.objects.prefetch_related("detailcart_set").filter(is_paid=False, user_id=request.user.id).first()
    total = cart.calculate_total_price()
    context = {
        'cart': cart,
        'total': total
    }

    return render(request, 'includes/cart_ajax.html', context=context)


#-----------------------------------------------PAYMENT-----------------------------------------------------




ZP_API_REQUEST = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://sandbox.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://sandbox.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "خرید محصول از سایت تاپ شاپ"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/cart/verify/'
MERCHANT = ''
@login_required
def send_request(request):
    current_cart, create = Cart.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_price = current_cart.calculate_total_price()
    if total_price == 0:
        return redirect(reverse('cart-page'))
    req_data = {
        "merchant_id": MERCHANT,
        "amount": total_price * 10,
        "callback_url": CallbackURL,
        "description": description,
        "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")

def verify(request):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    current_cart, create = Cart.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_price = current_cart.calculate_total_price()
    current_cart.saved_final_price()
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": total_price * 10,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                current_cart.is_paid = True
                current_cart.payment_date = time.time()
                current_cart.save()
                return render(request , 'cart_module/payment.html' , context={
                    'success':'تراکنش باموفقیت انجام شد!',
                    'ref_id' : req.json()['data']['ref_id']
                })
            elif t_status == 101:
                return render(request, 'cart_module/payment.html', context={
                    'info': 'تراکنش قبلا ثبت شده است!'
                })
            else:
                return render(request, 'cart_module/payment.html', context={
                    'error': req.json()['data']['message']
                })

        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return render(request, 'cart_module/payment.html', context={
                'error': e_message
            })
    else:
        return render(request, 'cart_module/payment.html', context={
            'error':'تراکنش با خظا مواجه شد یا کاربر از پرداخت منصرف شد!'
        })

#-----------------------------------------------PAYMENT-----------------------------------------------------