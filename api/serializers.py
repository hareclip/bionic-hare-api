from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import *


class CategorySerializer(serializers.ModelSerializer):
    """Category serializer
    """
    class Meta:
        model = Category
        fields = ['id', 'label']


class ArticleSerializer(serializers.ModelSerializer):
    """Article serializer
    """
    class Meta:
        model = Article
        fields = ['id', 'contents_file', 'title', 'header_image',
                  'category', 'author', 'date_created', 'date_edited', 'publisher']
