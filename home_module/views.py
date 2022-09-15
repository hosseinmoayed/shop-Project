from django.db.models import Count, Q, Prefetch, OuterRef, Subquery, Sum
from django.http import HttpResponse , JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
# Create your views here.
from django.views import View

from cart_module.models import Cart
from product_module.models import Product, ProductCategory
from utils.spliterlist import Group_list

from site_module.models import SiteSetting, FooterCategoryLink, Slider, AdsBanners



class Home(TemplateView):
    template_name = "home_module/index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter(is_active=True)

        context["sliders"] = sliders
        new_products = list(Product.objects.filter(is_active=True , is_delete=False).order_by("-id")[:8])
        context["new_products"] = Group_list(new_products)

        most_products_view = Product.objects.filter(is_delete=False , is_active=True).annotate(view_count = Count('productview')).order_by("-view_count")[:8]
        most_products_view = Group_list(most_products_view)
        context["most_product_view"] = most_products_view

        # categories = ProductCategory.objects.annotate(product_count= Count("product" , Q(is_active = True))).filter(is_delete=False , is_active=True , parent_id=None , product_count__gt = 0)[:5].prefetch_related(Prefetch('product_set',queryset= Product.objects.filter(is_active = True , is_delete=False)[0:3].order_by("-id")))
        categories = ProductCategory.objects.annotate(product_count = Count("product" , Q(is_active = True , is_delete=False))).filter(is_delete=False , is_active=True , parent_id=None)[:6]
        list_category_product = []
        for category in categories:
            list_category_product.append({
                'title': category.title,
                'id': category.id,
                "product": list(category.product_set.filter(is_active=True , is_delete=False).order_by("-id")[:4]),
                'url_title' : category.url_title
            })
        context["product_category"] = list_category_product

        best_seller_product = Product.objects.filter(detailcart__cart__is_paid=True).annotate(product_count = Sum('detailcart__count')).order_by('-product_count')[:12]
        context['best_seller_product'] = Group_list(best_seller_product)

        return context



def site_header(request):
    setting = SiteSetting.objects.filter(is_main_setting=True).first()
    count_product_in_cart = 0
    if request.user.is_authenticated:
        count_product_in_carts = Cart.objects.filter(is_paid=False , user_id=request.user.id).first()
        if count_product_in_carts is not None:
            count_product_in_cart = count_product_in_carts.detailcart_set.count()


    return render(request , 'shared/site_header.html' , context={
        'setting' : setting,
        'count_product_in_cart':count_product_in_cart
    })


def site_footer(request):
    setting = SiteSetting.objects.filter(is_main_setting=True).first()
    categort_link = FooterCategoryLink.objects.filter(is_active=True)
    return render(request , 'shared/site_footer.html' ,context={
        'setting':setting,
        'category_link' :categort_link
    })


class AboutUs(TemplateView):
    template_name = "home_module/abou_us.html"


    def get_context_data(self,*args ,**kwargs):
        context = super(AboutUs, self).get_context_data(*args ,**kwargs)
        setting = SiteSetting.objects.filter(is_main_setting=True).first()

        context["setting"] = setting
        context['banners'] = AdsBanners.objects.filter(is_active=True , position__iexact=AdsBanners.position_banner.about_us)
        return context

class Search_momentary(View):
    def get(self , request):
        search_text = request.GET.get("text")
        search_product = Product.objects.filter(title__icontains=search_text)[:6]

        search_product_momentary = [{'a': f'<a href="/products/{i.slug}" >{i.title}</a>'} for i in search_product]
        return JsonResponse({
            "result_search": search_product_momentary,
        })


    def post(self , request):
        pass


class Search(ListView):
    template_name = 'home_module/search_text.html'
    model = Product
    paginate_by = 20


    def get_queryset(self , **kwargs):
        query = super(Search, self).get_queryset()
        search = self.kwargs.get('text_search')

        if search is None:
            search = self.request.GET.get("search")
        query = query.filter(title__icontains=search)
        order = self.kwargs.get('sort')
        if order is not None:
            if order == 1:
                query = query.order_by('-price')
            elif order == 2:
                query = query.order_by('price')
            elif order == 3:
                query= query.order_by('-id')
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        search = self.kwargs.get('text_search')
        if search is None:
            search = self.request.GET.get("search")
        context['text_search'] = search

        return context