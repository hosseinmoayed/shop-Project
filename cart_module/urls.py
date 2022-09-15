# from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from django.urls import path , include
urlpatterns = [
    path("add-product-to-cart" , views.AddProductToCartView , name = "add_product_to_cart"),
    path("remove-from-cart" , views.RemovecartView , name = "remove_product"),
    path("change-product-count" , views.Change_cart_product_count , name = "change_product_count"),
    path('request/', views.send_request, name='request'),
    path('verify/', views.verify , name='verify')
]
