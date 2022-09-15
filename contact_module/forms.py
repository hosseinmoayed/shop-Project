from django import forms

from .models import ContactUs, Uploaded


# class CantactUSForm(forms.Form):
#     subject = forms.CharField(label="عنوان" ,max_length=50,widget=forms.TextInput(attrs={
#         "class" : "form-control",
#         "placeholder" : "عنوان"
#     }), error_messages={
#         'required' : "وارد کردن عنوان اجباریست",
#         'max-lenght' : "تعداد کاراکتر نمیتواد بیشتر از 50 باشد"
#     })
#     email = forms.EmailField(label= "ایمیل" , widget=forms.EmailInput(attrs={
#         'class' : "form-control",
#         "placeholder": "ایمیل"
#     }))
#     name = forms.CharField(label="نام و نام خانوادگی" , widget=forms.TextInput(attrs={
#         'class' : "form-control",
#         "placeholder": "نام و نام خانوادگی"
#     }) )
#     text = forms.CharField(label= "متن پیام" , widget=forms.Textarea(attrs={
#         "class" : "form-control",
#         "id" : "message",
#         "placeholder" : "متن پیام"
#     }))


class ContactUsFormModel(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["full_name" , "email" , "subject" , "message"]

        widgets = {
            "full_name" : forms.TextInput(attrs={
                'class' : "form-control",
                "placeholder": "نام و نام خانوادگی"
            }),
            "email" : forms.EmailInput(attrs={
                'class': "form-control",
                "placeholder": "ایمیل"
            }),
            "subject" : forms.TextInput(attrs={
                'class': "form-control",
                "placeholder": "عنوان"
            }),

            "message" :  forms.Textarea(attrs={
                "class": "form-control",
                "id": "message",
                "placeholder": "متن پیام"
            })
        }


# class ProfileForm(forms.Form):
#     user_image = forms.FileField()
