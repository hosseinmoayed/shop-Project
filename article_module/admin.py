from django.contrib import admin
from .models import ArticleCategory , Article , ArticleComment
# Register your models here.


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ["title" , "url_title" , "parent" , "is_active"]
    list_editable = ["url_title","parent" , 'is_active']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title" , "slug" ,"date" ,"writer","is_active"]
    list_editable = ["is_active"]

    def save_model(self, request, obj:Article, form, change):
        if not change:
            obj.writer = request.user
        if change:
            if obj.image == "":
                obj.image = "images/product/emty.jpg"
        super(ArticleAdmin, self).save_model(request, obj, form, change)

class CommentAdmin(admin.ModelAdmin):
    list_display = ["user","article","parent" , "date"]

admin.site.register(ArticleCategory , ArticleCategoryAdmin)
admin.site.register(Article , ArticleAdmin)
admin.site.register(ArticleComment , CommentAdmin)