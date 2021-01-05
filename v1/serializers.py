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
    contentsFileName = serializers.ImageField(source='contents_file')
    headerImageFileName = serializers.ImageField(source='header_image')
    dateCreated = serializers.DateTimeField(source='date_created')
    dateEdited = serializers.DateTimeField(source='date_edited')
    dateVisible = serializers.DateTimeField(source='date_created')
    categoryId = serializers.IntegerField(source='category.id')
    categoryLabel = serializers.CharField(source='category.label')
    fullName = serializers.SerializerMethodField('get_full_name')

    def get_full_name(self, article):
        return f'{article.author.first_name} {article.author.last_name}'.strip()

    class Meta:
        model = Article
        fields = ['id', 'contentsFileName', 'title', 'headerImageFileName',
                  'category', 'author', 'dateCreated', 'dateEdited', 'dateVisible', 'publisher', 'categoryId', 'categoryLabel', 'fullName']
