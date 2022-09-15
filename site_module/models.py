from django.db import models

# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200 , verbose_name="نام سایت")
    site_url = models.CharField(max_length=200 , verbose_name="دامنه سایت")
    address = models.TextField(verbose_name="آدرس ")
    image_map_address = models.ImageField(upload_to="images/site-setting" , verbose_name="تصویر نقشه ادرس شما",null=True,blank=True)
    phone = models.CharField(max_length=200,null=True , blank=True , verbose_name="تلفن سایت")
    fax = models.CharField(max_length=200 ,null=True , blank=True , verbose_name="فکس سایت")
    email = models.CharField(max_length=200 ,null=True , blank=True , verbose_name="ایمیل سایت")
    copy_right = models.CharField(max_length=300 , verbose_name="متن کپی رایت سایت")
    about_us = models.TextField(verbose_name="متن درباره ما سایت")
    site_logo = models.ImageField(upload_to="images/site-setting")
    is_main_setting = models.BooleanField(verbose_name="تنظیمات سایت")

    class Meta:
        verbose_name = "تنظیم سایت"
        verbose_name_plural = "تنظیمات سایت"

    def __str__(self):
        return self.site_name


class FooterCategoryLink(models.Model):
    title = models.CharField(max_length=200 , verbose_name="عنوان دسته بندی")
    is_active = models.BooleanField(verbose_name= "فعال / غیرفعال" , default=True)

    class Meta:
        verbose_name= "دسته بندی لینک"
        verbose_name_plural = "دسته بندی لینک ها"

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    url = models.URLField(max_length=600 , verbose_name="ادرس لینک")
    category = models.ForeignKey(to=FooterCategoryLink, on_delete=models.CASCADE , verbose_name="دسته بندی")

    class Meta:
        verbose_name = " لینک فوتر"
        verbose_name_plural = " لینک فوتر"

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=200 , verbose_name="عنوان اسلایدر")
    descriptions = models.TextField(verbose_name="توضیحات")
    url_title = models.CharField(max_length=200 , verbose_name="عنوان لینک")
    url = models.URLField(verbose_name="لینک")
    image = models.ImageField(upload_to="images/slider")
    is_active = models.BooleanField(verbose_name= "فعال / غیرفعال" , default=True)

    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدر ها"
    def __str__(self):
        return self.title



class AdsBanners(models.Model):
    class position_banner(models.TextChoices):
        product_list = 'product_list' , 'صفحه لیست محصولات'
        detail_view = 'product_detail' , 'صفحه جزییات محصول'
        about_us = 'about_us' , 'صفحه درباره ما'

    title = models.CharField(max_length=100 , verbose_name="عنوان بنر")
    url = models.URLField(verbose_name= "آدرس (url)",null=True , blank=True)
    image = models.ImageField(upload_to="images/banners" , verbose_name="تصویر بنر")
    position = models.CharField(max_length=200,choices= position_banner.choices, verbose_name="محل قرار گیری")
    is_active = models.BooleanField(verbose_name=" فعال / غیرفعال")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "بنرتبلیغ"
        verbose_name_plural = "بنرهای تبلیغاتی"