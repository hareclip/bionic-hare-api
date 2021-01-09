from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import *


class UserSerializer(serializers.ModelSerializer):
    """User serializer
    """

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class ArticleSerializer(serializers.ModelSerializer):
    """Article serializer
    """

    author = UserSerializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'contents_file', 'header_image',
                  'author', 'date_created', 'date_edited']


class CategorySerializer(serializers.ModelSerializer):
    """Category serializer
    """

    class Meta:
        model = Category
        fields = ['id', 'label']
