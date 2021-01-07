import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import *
from ..serializers import *
from ..utils import auth_decorator


@api_view(['POST'])
@auth_decorator({2, 3})
def check_auth(request):
    """Checks if supplied user credentials are valid
    """
    return Response('user is authorized', 200)


@api_view(['POST'])
@auth_decorator({2, 3})
def create_author(request):
    """Checks if supplied user credentials are valid
    """
    full_name = request.POST.get('fullName')
    if full_name == None:
        return Response('new author full name is required', 400)

    try:
        first_name, last_name = [v.strip() for v in full_name.split(' ')]
        user = User(
            username=uuid.uuid4(),
            first_name=first_name,
            last_name=last_name
        )
        user.set_unusable_password()
        user.save()
        AuthorProfile.objects.create(
            user=user,
            created_by=request.user,
        )
        return Response('user created', 201)
    except IntegrityError:
        return Response('user could not be created', 400)


@api_view(['POST'])
@auth_decorator({2, 3})
def publish_article(request):
    """Publishes article
    """
    # TODO: implement publish article
