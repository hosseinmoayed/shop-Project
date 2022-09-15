import home_module.urls
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView, CreateView, ListView

# from .forms import CantactUSForm
# Create your views here.
from django.urls import reverse

from site_module.models import SiteSetting
from .forms import ContactUsFormModel
from .models import ContactUs, Uploaded


class ContactUsView(CreateView):
    template_name = "contact_module/contact-us.html"
    form_class = ContactUsFormModel
    success_url = "/"

    def get_context_data(self, *args,**kwargs):
        context = super(ContactUsView, self).get_context_data(*args , *kwargs)
        setting = SiteSetting.objects.filter(is_main_setting=True).first()
        context["setting"] = setting
        return context



