from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from article_module import views
from django.conf.urls.static import static

urlpatterns = [
    path("" , views.ArticleView.as_view() , name = "list_article_page"),
    path("cat/<str:category>" , views.ArticleView.as_view() , name = "category_article_page"),
    path("article-comment" , views.Add_Comment , name = "article_comment"),
    path("<int:pk>" , views.DetailArticleView.as_view() , name = "article_deatil_page"),
]

