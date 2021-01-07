from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import *
from ..serializers import *
from ..utils import auth_decorator


@api_view(['POST'])
@auth_decorator({3})
def check_auth(request):
    """Checks if supplied user credentials are valid
    """
    return Response('user is authorized', 200)


@api_view(['POST'])
@auth_decorator({3})
def create_user(request):
    """Creates user
    """
    username = request.POST.get('newUsername')
    if username == None:
        return Response('new user username is required', 400)
    password = request.POST.get('newPassword')
    if password == None:
        return Response('new user password is required', 400)
    role = request.POST.get('newRole')
    if role == None:
        return Response('new user role is required', 400)

    # Parse role
    try:
        role = int(role)
    except ValueError:
        return Response('new user role must be integer', 400)

    try:
        User.objects.create(
            username=username,
            password=password,
            is_staff=(role >= 2),
            is_superuser=(role >= 3),
        )
        return Response('user created', 201)
    except IntegrityError:
        return Response('user could not be created', 400)


@api_view(['POST'])
@auth_decorator({3})
def delete_article(request):
    """Deletes article
    """
    article_id = request.POST.get('id')
    if article_id == None:
        return Response('id is required', 400)

    try:
        Article.objects.get(id=article_id).delete()
        return Response(None, 204)
    except ObjectDoesNotExist:
        return Response('could not find article', 404)
