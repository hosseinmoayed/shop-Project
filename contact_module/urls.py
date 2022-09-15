from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('' , views.ContactUsView.as_view() , name = "contact-us"),
    # path('profile' , views.CreateProfileView.as_view() , name = "profile-view"),

]


