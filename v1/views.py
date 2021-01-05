from django.shortcuts import render
from rest_framework import views, viewsets, permissions, status, mixins, filters
from rest_framework.response import Response
from core.models import *
from .serializers import *


class CategoryView(views.APIView):
    """Category view
    """

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({'data': {'categories': serializer.data, 'count': categories.count()}})


class ArticleView(views.APIView):
    """Article view
    """

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({'data': {'articles': serializer.data, 'count': articles.count()}})
