from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
from account_module.models import User


class ProductCategory(models.Model):
    title = models.CharField(max_length=300 , verbose_name="عنوان" , db_index=True)
    url_title = models.CharField(max_length=300 , verbose_name= "عنوان (url)" , db_index=True , unique=True)
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name="حذف شده / نشده")
    parent = models.ForeignKey('ProductCategory' , on_delete=models.CASCADE , verbose_name=  "زیر مجموعه", null=True , blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class ProductBrand(models.Model):
    title = models.CharField(max_length=200 , verbose_name='برند')
    url_title = models.CharField(max_length=100 , verbose_name= "عنوان (url)" , db_index=True , blank=True , null=True)
    is_active = models.BooleanField(default=True , verbose_name='فعال / غیرفعال')
    category = models.ManyToManyField(ProductCategory ,verbose_name="دسته بندی")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "برند "
        verbose_name_plural = " برند ها"


class Product(models.Model):
    title = models.CharField(max_length=300 , verbose_name="نام محصول")
    category = models.ManyToManyField(ProductCategory , verbose_name="دسته بندی")
    brand = models.ForeignKey(ProductBrand , on_delete=models.CASCADE , null=True , blank=True)
    price = models.IntegerField(verbose_name='قیمت')
    short_discription = models.CharField(max_length=360 , verbose_name= 'توضیحات کوتاه' , db_index=True)
    main_discription = models.TextField(max_length=360, verbose_name=' توضیحات اصلی' , db_index=True)
    image = models.ImageField(upload_to="images/product", verbose_name="تصویر محصول", null=True, blank=True)
    slug = models.SlugField(default="", null=False, blank=True, unique=True, max_length=200)
    is_active = models.BooleanField(default=False , verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name="حذف شده / نشده")

    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super().save(*args , **kwargs)

    def __str__(self):
        return f"{self.title}"

    def get_absolut_url(self):
        return reverse('product-list' , args=[self.slug])
    class Meta:
        verbose_name =" محصول"
        verbose_name_plural = "محصولات"

class ProductTag(models.Model):
    tag_name = models.CharField(max_length=300 , verbose_name= 'نام تگ' , db_index=True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE , verbose_name="محصول")
    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = "تگ"
        verbose_name_plural = " تگ ها "


class ProductView(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , verbose_name="محصول")
    user_ip = models.CharField(max_length=70 , verbose_name="آیپی کاربر")
    user = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name=  "کاریر",null=True ,blank=True )

    class Meta:
        verbose_name = "بازدید"
        verbose_name_plural = 'بازدیدها'

    def __str__(self):
        return self.product


class ProductGallery(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , verbose_name="محصول")
    image = models.ImageField(upload_to="images/product_gallery" , verbose_name="تصویر")

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "گالری تصاویر"


class AddCommentProduct(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , verbose_name="محصول")
    parent = models.ForeignKey("AddCommentProduct" , on_delete=models.CASCADE ,null=True , blank=True, verbose_name="پاسخ")
    user = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name="کاربر" )
    message = models.TextField(verbose_name="متن نظر")
    date = models.DateTimeField(verbose_name= "تاریخ" , auto_now_add=True)
    is_confirmed = models.BooleanField(verbose_name="تایید شده / نشده", default=False)
    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"



    def __str__(self):
        return str(self.user)
