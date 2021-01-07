from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import *
from ..serializers import *


@api_view(['GET'])
def list_all(request):
    """Gets all authors
    """
    profiles = AuthorProfile.objects.all()
    serializer = AuthorProfileSerializer(profiles, many=True)
    return Response({'data': {'authors': serializer.data, 'count': profiles.count()}})
