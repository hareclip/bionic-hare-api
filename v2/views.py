from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import *


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """Author view
    """
    lookup_field = 'id'
    queryset = User.objects.filter(
        Q(profile__is_author=True) & Q(is_active=True)
    )
    serializer_class = UserSerializer


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """Article view
    """
    lookup_field = 'id'
    queryset = Article.objects.filter(is_visible=True)
    serializer_class = ArticleSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Category view
    """
    lookup_field = 'id'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
