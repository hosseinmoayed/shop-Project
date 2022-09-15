from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from article_module.models import Article, ArticleCategory, ArticleComment


# Create your views here.


class ArticleView(ListView):
    template_name = "article_madule/article_list_page.html"
    model = Article
    ordering = ["-date"]
    paginate_by = 5

    def get_queryset(self):
        data_bases = super(ArticleView, self).get_queryset()
        category = self.kwargs.get("category")
        data_base = data_bases.filter(is_active=True)
        if category is not None:
            data_base = data_bases.filter(is_active=True , category__url_title = category)
            return data_base
        return data_base


class DetailArticleView(DetailView):
    template_name = "article_madule/detai_article.html"
    model = Article

    def get_queryset(self):
        articles = super(DetailArticleView, self).get_queryset()
        articles = articles.filter(is_active = True)
        return articles
    def get_context_data(self, **kwargs):
        context = super(DetailArticleView, self).get_context_data(**kwargs)
        article = kwargs.get("object")
        context["comments"] = ArticleComment.objects.filter(article_id=article.id , parent_id = None , is_confirmed=True).prefetch_related('articlecomment_set').order_by("-date")
        context["comments_count"] = ArticleComment.objects.filter(article_id=article.id , is_confirmed=True).count()
        return context




def category_partial(request):
    main_category = ArticleCategory.objects.prefetch_related("articlecategory_set").filter(is_active=True , parent_id = None)
    context = {
        'main_category' : main_category
    }
    return render(request , 'includes/article_category.html' , context)



def Add_Comment(request):
    if request.user.is_authenticated:
        data = request.GET
        text = data.get("text")
        article_id = data.get("article_id")
        user_id = request.user.id
        parent_id = data.get("parent_id")
        ArticleComment.objects.create(text=text , article_id=article_id , user_id=user_id , parent_id=parent_id , is_confirmed=True)
        context = {
            "comments" : ArticleComment.objects.prefetch_related('articlecomment_set').filter(article_id=article_id , parent_id = None , is_confirmed=True).order_by("-date"),
            "comments_count" : ArticleComment.objects.filter(article_id=article_id , is_confirmed=True).count()
        }
        return render(request , "includes/comments_ajax.html" , context)
    return HttpResponse("RESPONSE")









