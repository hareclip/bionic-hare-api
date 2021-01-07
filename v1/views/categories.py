from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import *
from ..serializers import *


@api_view(['GET'])
def list_all(request):
    """Gets total article count
    """
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response({'data': {'categories': serializer.data, 'count': categories.count()}})


@api_view(['GET'])
def get_by_id(request, category_id):
    """Gets total article count
    """
    try:
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category)
        return Response({'data': serializer.data})
    except ObjectDoesNotExist:
        return Response('category not found', 404)
