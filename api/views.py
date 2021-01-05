from api.serializers import CategorySerializer
from django.shortcuts import render
from rest_framework import viewsets, permissions, status, mixins, filters
from core.models import *
from .serializers import *


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Category view
    """
    lookup_field = 'id'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """Article view
    """
    lookup_field = 'id'
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
