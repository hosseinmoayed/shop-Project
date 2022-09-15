from django.contrib import admin
from . import models
# Register your models here.
# from sorl.thumbnail.admin import AdminImageMixin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title' , "price" , "is_active" , "is_delete"]
    list_editable = ['is_active' , 'price']
    list_filter = ['is_active' , "category"]
    # def save_model(self, request, obj: Product, form, change):
    #     if change:
    #         if obj.avatar == "":
    #             obj.avatar = "images/profile/profile_lq7IBip.jpg"
    #     super(UserAdmin, self).save_model(request, obj, form, change)
    def save_model(self, request, obj: Product, form, change):
        if change:
            if obj.image == "":
                obj.image = "images/product/emty.jpg"
        super(ProductAdmin, self).save_model(request, obj, form, change)

    # prepopulated_fields = {
    #     'product_dic' : ['title']
    # }

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ["title" , "url_title"]

class Product_View_Admin(admin.ModelAdmin):
    list_display = ['product' , 'user_id' , 'user_id']

admin.site.register(models.ProductCategory)
admin.site.register(models.Product , ProductAdmin)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand)
admin.site.register(models.ProductView)
admin.site.register(models.ProductGallery)
admin.site.register(models.AddCommentProduct)

