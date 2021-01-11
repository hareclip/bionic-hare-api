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
    queryset = Article.objects.filter(
        is_visible=True).order_by('-date_created')
    serializer_class = ArticleSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get('search_term')
        category_id = self.request.query_params.get('category_id')

        queryset = super().get_queryset()

        if search_term:
            queryset = queryset.filter(
                Q(title__icontains=search_term) |
                Q(author__first_name=search_term) |
                Q(author__last_name=search_term)
            )
        if category_id:
            queryset = queryset.filter(category__id=category_id)

        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Category view
    """
    lookup_field = 'id'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
