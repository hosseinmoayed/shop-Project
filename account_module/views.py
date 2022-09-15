from django.contrib.auth import login , logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView , TemplateView , FormView
from utils.email_service import send_email
from account_module.forms import CreateAccountForm, LoginForm, Forgot_pass_form, ResetPassForm
from account_module.models import User
from django.utils.crypto import get_random_string

class CreateAccountView(CreateView):
    template_name = "account_module/create_account.html"
    form_class = CreateAccountForm
    success_url = reverse_lazy("login-page")


class LoginView(View):
    def get(self , request):
        classform = LoginForm()

        return render(request , 'account_module/login.html' , context={
            'login_form' : classform
        })

    def post(self , request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get("email")
            password = login_form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=email).first()
            if user is not None:
                check_password = user.check_password(password)
                if check_password:
                    login(request , user)
                    return redirect(reverse("home_page"))

                else:
                    login_form.add_error("password" , "حسابی با این اطلاعات یافت نشد")
            else:
                login_form.add_error("email" , "حسابی با این اطلاعات یافت نشد")

        return render(request, 'account_module/login.html', context={
            'login_form': login_form
        })


class ActiveAccountView(View):
    def get(self , request , active_code):
        check_user = User.objects.filter(active_email_code__iexact=active_code).first()
        if check_user is not None:
            if not check_user.is_active:
                check_user.is_active = True
                check_user.active_email_code = get_random_string(72)
                check_user.save()
                return redirect(reverse("login-page"))

class ForgotPasswordView(View):
    def get(self , request):
        forgot_pass = Forgot_pass_form()
        return render(request , 'account_module/forgot_password.html' , context={
            'forgot_pass' : forgot_pass
        })

    def post(self , request):
        forgot_pass = Forgot_pass_form(request.POST)
        if forgot_pass.is_valid():
            user_email = forgot_pass.cleaned_data.get("email")
            user = User.objects.filter(email__iexact=user_email).first()
            print(user)
            if user is not None:
                print(f"ok > {user}")
                send_email("بازیابی حساب کاربری" ,to = user.email , context= {'user' : user} , templatename= "account_module/reset_pass_email.html" )
                forgot_pass = Forgot_pass_form()
                return render(request, 'account_module/forgot_password.html', context={
                    'forgot_pass': forgot_pass
                })

            else:
                forgot_pass.add_error("email" , "حسابی با این ایمیل یافت نشد")


class ResetPasswordView(View):
    def get(self , request , reset_pass_code):
        user = User.objects.filter(active_email_code__iexact=reset_pass_code).first()
        if user is not None:
            reset_pass_form = ResetPassForm()
            return render(request , 'account_module/reset_password.html' , context={
                'reset_pass_form' : reset_pass_form,
                "user" : user
            })
        else:
            return redirect(reverse("login-page"))

    def post(self , request , reset_pass_code):
        reset_pass_form = ResetPassForm(request.POST)
        user = User.objects.filter(active_email_code__iexact=reset_pass_code).first()
        if reset_pass_form.is_valid():
            password = reset_pass_form.cleaned_data.get("password")
            confirm_password = reset_pass_form.cleaned_data.get("confirm_password")
            if password == confirm_password:
                if user is not None:
                    user.set_password(password)
                    user.active_email_code = get_random_string(72)
                    user.is_active = True
                    user.save()
                    return redirect(reverse("home_page"))
                else:
                    return redirect(reverse("login-page"))
            else:
                reset_pass_form.add_error("confirm_password" , "پسورد ها مغایرت دارند.")
        else:
            reset_pass_form = ResetPassForm()
            return render(request, 'account_module/reset_password.html', context={
                'reset_pass_form': reset_pass_form,
                "user": user
            })


class LogoutView(View):
    def get(self , request):
        logout(request)
        return redirect(reverse("login-page"))




