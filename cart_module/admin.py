from django.contrib import admin

# Register your models here.
from cart_module.models import Cart, DetailCart


class CartAdmin(admin.ModelAdmin):
    list_display = ["user" , "is_paid" , "payment_date"]


class DetailCartAdmin(admin.ModelAdmin):
    list_display = ["cart" , "product" , "final_price" , "count"]

admin.site.register(Cart , CartAdmin)
admin.site.register(DetailCart , DetailCartAdmin)
