
from django import forms
from account_module.models import User



class EditInformationsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name" , "last_name" , "address" , "avatar" , 'about_user']
        labels = {
            'avatar' : 'تصویر پروفایل'
        }
        widgets = {
            'first_name':forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'نام',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'آدرس',
                'rows' : 3
            }),
            'about_user':forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : "درباره من ",
                'rows' : 6
            }),
            'avatar':forms.FileInput(attrs={
                'class' : 'form-control'
            })
        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder':'پسورد فعلی'
    }),label="پسورد فعلی")

    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'پسورد جدید'
    }), label="پسورد جدید")

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'تکرار پسورد'
    }), label="تکرار پسورد")


    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password != confirm_password:
            raise forms.ValidationError({
                'confirm_password' : 'پسورد ها باهم مغیرت دارند'
            })
