from django.db import models

# Create your models here.


class ContactUs(models.Model):
    full_name = models.CharField(max_length=300 , verbose_name="نام")
    email = models.EmailField(max_length=300 , verbose_name="ایمیل")
    subject = models.CharField(max_length=400 , verbose_name="موضوع")
    message = models.TextField(verbose_name="متن پیام")
    is_read = models.BooleanField(default=False , verbose_name="خوانده شده/ نشده")
    create_date = models.DateTimeField(verbose_name=  "تاریخ ایجاد" , auto_now_add=True)
    response = models.TextField(verbose_name="متن پاسخ" , null=True , blank=True)
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name = "تماس با ما "
        verbose_name_plural = " لیست تماس با ما "


class Uploaded(models.Model):
    image = models.FileField(upload_to="images")