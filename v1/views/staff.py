import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
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

        user.profile.is_author = True
        user.profile.created_by = request.user
        user.save()
        return Response('user created', 201)
    except IntegrityError:
        return Response('user could not be created', 500)


@api_view(['POST'])
@auth_decorator({2, 3})
def publish_article(request):
    """Publishes article
    """
    title = request.POST.get('title')
    if title == None:
        return Response('title is required', 400)
    category_id = request.POST.get('category')
    if title == None:
        return Response('category is required', 400)
    author_id = request.POST.get('author')
    if title == None:
        return Response('author is required', 400)
    contents_file = request.FILES.get('contents')
    if contents_file == None:
        return Response('contents is required', 400)
    header_image = request.FILES.get('headerImage')
    if header_image == None:
        return Response('headerImage is required', 400)

    # Parse ids
    try:
        category_id = int(category_id)
    except ValueError:
        return Response('category must be integer', 400)
    try:
        author_id = int(author_id)
    except ValueError:
        return Response('author must be integer', 400)

    # Find objects by id
    try:
        category = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
        return Response('category not found', 400)
    try:
        author = User.objects.get(
            Q(id=author_id) &
            Q(profile__is_author=True)
        )
    except ObjectDoesNotExist:
        return Response('author not found', 400)

    try:
        article = Article.objects.create(
            title=title,
            category=category,
            author=author,
            publisher=request.user,
            contents_file=contents_file,
            header_image=header_image,
        )
        return Response(article.id, 201)
    except IntegrityError:
        return Response('article could not be created', 400)
