from django.contrib import admin
from .models import SiteSetting, Slider, AdsBanners
from .models import FooterCategoryLink , FooterLink
# Register your models here.

class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ["title" , "url"]
class SliderAdmin(admin.ModelAdmin):
    list_display = ["title" , "descriptions" , "url_title" , "url" , "image" , "is_active"]
    list_editable = ["url" , "is_active"]

class BannerAdmin(admin.ModelAdmin):
    list_display = ["title" , 'url' , 'position' , 'is_active']

admin.site.register(SiteSetting)
admin.site.register(FooterCategoryLink)
admin.site.register(Slider , SliderAdmin)
admin.site.register(AdsBanners , BannerAdmin)
admin.site.register(FooterLink , FooterLinkAdmin)