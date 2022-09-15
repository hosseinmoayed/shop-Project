from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('create-account' , views.CreateAccountView.as_view() , name = "create-account"),
    path('login' , views.LoginView.as_view() , name = "login-page"),
    path('logout' , views.LogoutView.as_view() , name = "login-out"),
    path('forgot-password' , views.ForgotPasswordView.as_view() , name = "forgot-page"),
    path('reset-password/<reset_pass_code>' , views.ResetPasswordView.as_view() , name = "reset-page"),
    path('activate-email-code/<active_code>' , views.ActiveAccountView.as_view() , name = "activate-email-page"),


]
