
from django import forms
from django.core import validators
from account_module.models import User
from utils.email_service import send_email
from django.utils.crypto import get_random_string

class CreateAccountForm(forms.ModelForm):
    confirm_password = forms.CharField(label="تکرار کلمه عبور" , widget=forms.PasswordInput(attrs={
        'placeholder' : "تکرار کلمه عبور"
    }))
    class Meta:
        model = User
        fields = ["email" , "password"]
        labels = {
            'email' : "ایمیل",
            'password' : "کلمه عبور"
        }
        widgets = {
            'password' : forms.PasswordInput(attrs={
                'placeholder' : "کلمه عبور"
            }),
            'email' : forms.EmailInput(attrs={
                'placeholder' : "ایمیل"
            }),

        }


    def __init__(self , *args , **kwargs):
        super(CreateAccountForm, self).__init__(*args , **kwargs)
        self.fields["email"].validators = [validators.MaxLengthValidator(100)]
        self.fields["password"].validators = [validators.MaxLengthValidator(100) , validators.MinLengthValidator(8)]

    def clean(self):
        cleaned_data = super(CreateAccountForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            # crate_acc.add_error('confirm_password', 'پسورد ها باهم مغایرت دارند.')
            raise forms.ValidationError(message={
                'confirm_password' : "پسورد ها باهم مغایرت دارند."
            })


        email = cleaned_data.get("email")

        check : bool = User.objects.filter(email__iexact=email).exists()
        if check:
            raise forms.ValidationError(message={
                'email' : "ایمیل وارد شده تکراری میباشد."
            })


        return cleaned_data

    def save(self, commit=True):
        user = super(CreateAccountForm, self).save(commit = True)
        user.active_email_code = get_random_string(72)
        user.username = self.cleaned_data.get("email")
        user.is_active = False
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        send_email("فعال سازی حساب کاربری" ,to = user.email , context= {'user' : user} , templatename= "account_module/active_email.html" )
        return user




class LoginForm(forms.Form):
    email = forms.EmailField(label= "ایمیل" ,validators=[validators.MaxLengthValidator(100) , validators.EmailValidator], widget=forms.EmailInput(attrs={
        'placeholder' : "ایمیل",
    }))

    password = forms.CharField(label= "کلمه عبور" ,validators=[validators.MaxLengthValidator(100)] ,widget=forms.PasswordInput(attrs={
        'placeholder' : "کلمه عبور"
    }))

class Forgot_pass_form(forms.Form):
    email = forms.EmailField(label= "ایمیل" ,validators=[validators.MaxLengthValidator(100) , validators.EmailValidator], widget=forms.EmailInput(attrs={
        'placeholder' : "ایمیل",
    }))


class ResetPassForm(forms.Form):
    password = forms.CharField(label=" کلمه عبور", widget=forms.PasswordInput(attrs={
        'placeholder': " کلمه عبور"
    }))
    confirm_password = forms.CharField(label="تکرار کلمه عبور", widget=forms.PasswordInput(attrs={
        'placeholder': "تکرار کلمه عبور"
    }))