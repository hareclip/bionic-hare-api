from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import categories, articles

urlpatterns = [
    path('categories/', categories.CategoryView.as_view()),

    path('articles/count/', articles.get_count),
    path('articles/search/', articles.search),
    path('articles/recent/', articles.get_recent),
    path('articles/home/', articles.get_home),
    path('articles/category/<int:category_id>/', articles.get_by_category),
    path('articles/<int:article_id>/', articles.get_by_id),
    path('articles/', articles.list_all),
]
