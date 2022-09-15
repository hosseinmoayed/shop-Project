from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from product_module.models import Product, ProductCategory, ProductBrand, ProductView, ProductGallery, AddCommentProduct
from django.db.models import Avg, Min, Max, Count, Q

from django.views.generic import ListView , DetailView

# Create your views here.
from site_module.models import AdsBanners
from utils.UserIP_Service import Get_Client_IP
from utils.spliterlist import Group_list
class ListProductView(ListView):
    template_name = "product_module/product_list.html"
    model = Product
    ordering = ["-price"]
    paginate_by = 6
    def get_queryset(self , **kwargs):
        base_data = super(ListProductView, self).get_queryset()
        category = self.kwargs.get("cat")
        brand = self.kwargs.get('brand')

        if category is not None and brand is None:
            base_data = base_data.filter(category__url_title__iexact=category,is_active = True)

        if brand is not None and category is not None:
            base_data = base_data.filter(brand__url_title__iexact=brand, is_active=True , category__url_title__iexact=category)

        start_price = self.request.GET.get("start_price")
        end_price = self.request.GET.get("end_price")
        if start_price is not None and end_price is not None:
            base_data = base_data.filter(price__gte = start_price , price__lte = end_price)

        order = self.kwargs.get('sort')
        if order is not None:
            if order == 1:
                base_data = base_data.order_by('-price')
            elif order == 2:
                base_data = base_data.order_by('price')
            elif order == 3:
                base_data = base_data.order_by('-id')
        return base_data

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListProductView, self).get_context_data(object_list=None, **kwargs)
        category = self.kwargs.get("cat")
        product = self.get_queryset()
        products = product.order_by("-price").first()
        context["start_price"] = self.request.GET.get("start_price") or 0 if products else 0
        context["end_price"] = self.request.GET.get("end_price") or products.price  if products else Product.objects.all().order_by("-price").first().price

        if category is not None:
            brands = ProductBrand.objects.filter(category__url_title__iexact=category).annotate(product_count = Count('product' , Q(product__category__url_title=category)))
            context['brands'] = brands
            context['brand'] = self.kwargs.get('brand')
            context['category'] = category
            return context
        context["banners"] = AdsBanners.objects.filter(is_active=True,position__iexact=AdsBanners.position_banner.product_list)

        return context





class ProductDetailView(DetailView):
    template_name = "product_module/product_detail.html"
    model = Product


    def get_queryset(self):
        products = super(ProductDetailView, self).get_queryset()
        products = products.filter(is_active = True)
        return products

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        context['banners'] = AdsBanners.objects.filter(is_active=True,position__iexact=AdsBanners.position_banner.detail_view)
        product_id = self.object.id
        if self.request.user.is_authenticated:
            user_id = self.request.user
        else:
            user_id = None
        user_ip = Get_Client_IP(self.request)
        check_user = ProductView.objects.filter(user_ip__iexact=user_ip , product_id = product_id).exists()
        if not check_user:
            ProductView.objects.create(product_id=product_id , user_ip=user_ip , user_id=user_id.id)

        products_gallery = ProductGallery.objects.filter(product_id=product_id)

        context["products_gallery_group"] = Group_list(products_gallery , 3 , main_image=self.object.image)
        product = Product.objects.get(id =self.object.id)
        category_type = product.category.filter(is_delete=False , is_active=True).exclude(parent_id=None).first()
        related_products = Product.objects.filter(category__id=category_type.id).exclude(id=self.object.id)
        context["related_products"]= Group_list(related_products,3)

        comments = AddCommentProduct.objects.filter(is_confirmed=True , product_id = self.object.id).order_by("-date")
        context["comments"] = comments
        context["count_comment"] = comments.count()
        return context

def AddCommentView(request):
    print(request)
    if request.user.is_authenticated:
        print(request)
        message = request.GET.get("message")
        product_id  = request.GET.get("product_id")
        AddCommentProduct.objects.create(product_id=product_id , message=message , user_id=request.user.id , is_confirmed=True)
        comments = AddCommentProduct.objects.filter(is_confirmed=True ,product_id=product_id ).order_by("-date")
        context = {
            'comments':comments,
        }
        return render(request , 'includes/ajax_comments_product.html' ,context=context)
    return HttpResponse("RESPONSE")







def product_category_partial(request):
    main_category = ProductCategory.objects.prefetch_related("productcategory_set").filter(is_active=True,
                                                                                           parent_id=None)
    return render(request, 'includes/product_category.html', context={
        'categories': main_category
    })






































