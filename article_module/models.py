import datetime

from django.db import models
from account_module.models import User
# Create your models here.


class ArticleCategory(models.Model):
    title = models.CharField(max_length=200 , verbose_name="عنوان دسته بندی")
    url_title = models.CharField(max_length=200 , verbose_name=  "عنوان (url)" , unique=True)
    parent = models.ForeignKey("ArticleCategory", on_delete=models.CASCADE, verbose_name="زیر مجموعه" ,blank=True ,null=True)
    is_active = models.BooleanField(default=True , verbose_name="فعال / غیرفعال")
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=300 , verbose_name="عنوان")
    writer = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name="نویسنده" , null=True , editable=False)
    slug = models.SlugField(max_length=400 , allow_unicode=True , db_index=True)
    image = models.ImageField(upload_to="hmage/article" , verbose_name="تصویر مقاله")
    short_descriptions = models.TextField(verbose_name="توضیحات کوتاه")
    text = models.TextField(verbose_name="متن مقاله")
    is_active = models.BooleanField(default=True , verbose_name="فعال / غیرفعال")
    category = models.ManyToManyField(to = ArticleCategory , verbose_name="دسته بندی")
    date = models.DateTimeField(auto_now_add=True ,editable=False, verbose_name= "زمان انتشار")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    article = models.ForeignKey(Article , on_delete=models.CASCADE , verbose_name="مقاله")
    parent = models.ForeignKey("ArticleComment" , on_delete=models.CASCADE , null=True , blank=True , verbose_name="پاسخ")
    user = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name= "کاربر")
    text = models.TextField(verbose_name="متن نظر")
    date = models.DateTimeField(auto_now_add=True , editable=False , verbose_name="تاریخ")
    is_confirmed = models.BooleanField(verbose_name="تایید شده / نشده" , default=False)

    class Meta:
        verbose_name = "نظر مقاله"
        verbose_name_plural = "نظرات مقاله"

    def __str__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        else:
            return self.user.email
