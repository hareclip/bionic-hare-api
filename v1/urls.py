from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view()),
    path('articles/', views.ArticleView.as_view()),
]
