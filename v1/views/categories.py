from rest_framework import views, permissions, status, mixins, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import *
from ..serializers import *


class CategoryView(views.APIView):
    """Category view
    """

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({'data': {'categories': serializer.data, 'count': categories.count()}})
