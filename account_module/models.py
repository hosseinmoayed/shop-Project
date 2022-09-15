from django.db import models
from django.contrib.auth.models import AbstractUser , AbstractBaseUser
# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to="images/profile" , verbose_name="تصویر آواتار" , null=True , blank=True)
    active_email_code = models.CharField(max_length=200 , verbose_name= "کد فعالسازی ایمیل")
    about_user = models.TextField(null=True , blank=True , verbose_name="درباره شخص")
    address = models.TextField(null=True , blank=True , verbose_name="آدرس")
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"


    def __str__(self):
        if self.first_name == '' and self.last_name == '':
            return self.email
        return str(self.get_full_name())

    def save(self, *args, **kwargs):
        if self.avatar == "":
            self.avatar = "images/profile/profile_lq7IBip.jpg"
        super(User, self).save(*args, **kwargs)




