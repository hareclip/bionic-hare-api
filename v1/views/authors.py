from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import *
from ..serializers import *


@api_view(['GET'])
def list_all(request):
    """Gets all authors
    """
    authors = User.objects.filter(
        Q(profile__is_author=True) & Q(is_active=True)
    )
    serializer = UserSerializer(authors, many=True)
    return Response({'data': {'authors': serializer.data, 'count': authors.count()}})
