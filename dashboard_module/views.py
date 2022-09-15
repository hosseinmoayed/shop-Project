from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from account_module.models import User
from cart_module.models import Cart
from dashboard_module.forms import EditInformationsForm, ChangePasswordForm

@method_decorator(login_required , 'dispatch')
class Dashboard(TemplateView):
    template_name = "dashboard_module/dashboard.html"


@method_decorator(login_required , 'dispatch')
class EditInformationsView(View):
    def get(self , request):
        if request.user.is_authenticated:
            user_info = User.objects.get(id=request.user.id)
            edit_info = EditInformationsForm(instance = user_info)
            context = {
                'form' : edit_info,
                'user_info' : user_info
            }
            return render(request , "dashboard_module/edit_informations.html" , context)
    def post(self , request):
        if request.user.is_authenticated:
            user_info = User.objects.get(id=request.user.id)
            edit_info = EditInformationsForm(request.POST , request.FILES , instance=user_info)
            if edit_info.is_valid():
                edit_info.save()
            context = {
                'form': edit_info,
                'user_info' : user_info
            }
            return render(request, "dashboard_module/edit_informations.html", context)

@method_decorator(login_required , 'dispatch')
class ChangePassword(View):
    def get(self , request):
        form = ChangePasswordForm()
        context = {
            'form' : form
        }
        return render(request , 'dashboard_module/change_password.html' , context)

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id = request.user.id)
            current_password = form.cleaned_data.get("current_password")
            if user.check_password(current_password):
                user.set_password(form.cleaned_data.get("new_password"))
                user.save()
                logout(request)
                return redirect(reverse('login-page'))

            else:
                form.add_error('current_password', 'رمز فعلی اشتباه است')
        context = {
            'form': form
        }
        return render(request, 'dashboard_module/change_password.html', context)

@login_required
def CartView(request):
    cart, create = Cart.objects.prefetch_related("detailcart_set").get_or_create(user_id=request.user.id , is_paid=False)

    total = cart.calculate_total_price()
    context = {
        'cart' : cart,
        'total' : total
    }

    return render(request , 'dashboard_module/cart.html' , context)


@method_decorator(login_required , 'dispatch')
class Past_Shopping(ListView):
    template_name = 'dashboard_module/past_shopping.html'
    model = Cart

    def get_queryset(self):
        query = super(Past_Shopping, self).get_queryset()
        query = query.filter(user_id = self.request.user.id , is_paid = True).order_by('-payment_date')
        return query


def Cart_Detail(request , cart):

    return render(request ,'dashboard_module/detail.html' , context = {
        'cart' : Cart.objects.prefetch_related('detailcart_set').filter(id = cart , user_id=request.user.id).first()
    })

