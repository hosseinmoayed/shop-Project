from django.contrib import admin

# Register your models here.
from account_module.models import User


class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj: User, form, change):
        if change:
            if obj.avatar == "":
                obj.avatar = "images/profile/profile_lq7IBip.jpg"
        super(UserAdmin, self).save_model(request, obj, form, change)

admin.site.register(User , UserAdmin)