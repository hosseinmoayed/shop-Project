from django.db import models

# Create your models here.
from account_module.models import User
from product_module.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name="کاربر")
    is_paid = models.BooleanField(verbose_name="پرداخت شده/ نشده")
    payment_date = models.DateTimeField(null=True , blank=True , verbose_name="تاریخ پرداخت")
    class Meta:
        verbose_name="سبد خرید"
        verbose_name_plural = "لیست سبد خرید"

    def calculate_total_price(self):
        total_price = 0
        if self.is_paid:
            for product_detail in self.detailcart_set.all():
                total_price += product_detail.final_price * product_detail.count
        else:
            for product_detail in self.detailcart_set.all():
                total_price += product_detail.product.price* product_detail.count
        return total_price

    def saved_final_price(self):
        for product_detail in self.detailcart_set.all():
            product_detail.final_price = product_detail.product.price
            product_detail.save()

    def __str__(self):
        return str(self.user)


class DetailCart(models.Model):
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE , verbose_name="سبد خرید")
    product = models.ForeignKey(Product , on_delete=models.CASCADE , verbose_name="محصول")
    final_price = models.IntegerField(verbose_name="قیمت نهایی"  , null=True , blank=True)
    count = models.IntegerField(verbose_name="تعداد")


    def __str__(self):
        return str(self.product) +" / "+ str(self.cart.user)

    def get_total_price(self):
        return self.count * self.product.price



    class Meta:
        verbose_name = "جزِِییات محصول"
        verbose_name_plural = "لیست جزییات محصول ها"

