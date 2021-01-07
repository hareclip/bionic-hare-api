from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import *
from ..serializers import *


@api_view(['GET'])
def list_all(request):
    """Gets all authors
    """
    # TODO: add authors
