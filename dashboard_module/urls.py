# from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from django.urls import path , include
urlpatterns = [
    path('' , views.Dashboard.as_view() , name = "dashboard-panel"),
    path('edit_informations' , views.EditInformationsView.as_view() , name = "edit_informations"),
    path('change-password' , views.ChangePassword.as_view() , name = "change-password"),
    path('past-shopping' , views.Past_Shopping.as_view() , name = "past-shopping"),
    path('cart' , views.CartView, name = "cart-page"),
    path('cart-detail/<cart>' , views.Cart_Detail, name = "cart-detail-page"),

]
