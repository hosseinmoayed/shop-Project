from django.urls import path , include
from . import views
urlpatterns = [
    path('' , views.Home.as_view(), name = "home_page"),
    path('about-us' , views.AboutUs.as_view() , name = "about-page"),
    path('search_momentary' , views.Search_momentary.as_view() , name = "search-momentary"),
    path('search/<str:text_search>' , views.Search.as_view() , name = "search-page"),
    path('search/<str:text_search>/<int:sort>' , views.Search.as_view() , name = "search-sort"),


]
