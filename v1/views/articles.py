from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import *
from ..serializers import *


num_articles = 6


@api_view(['GET'])
def get_count(request):
    """Gets total article count
    """
    articles = Article.objects.filter(is_visible=True)
    return Response({'data': {'count': articles.count()}})


@api_view(['GET'])
def search(request):
    """Search articles
    """
    search_term = request.GET.get('searchTerm')

    if search_term == None:
        return Response('searchTerm is required', 400)

    # TODO: mirror article content in db and replace with full-text search?
    articles = Article.objects.filter(
        (
            Q(title__icontains=search_term) |
            Q(author__first_name=search_term) |
            Q(author__last_name=search_term)
        ) & Q(is_visible=True)
    ).order_by('-date_created')[:num_articles]
    serializer = ArticleSerializer(articles, many=True)
    return Response({'data': {'articles': serializer.data, 'count': articles.count()}})


@api_view(['GET'])
def get_by_category(request, category_id):
    """Gets articles by category
    """
    articles = Article.objects.filter(
        Q(category__id=category_id) & Q(is_visible=True)
    ).order_by('-date_created')[:num_articles]
    serializer = ArticleSerializer(articles, many=True)
    return Response({'data': {'articles': serializer.data, 'count': articles.count()}})


@api_view(['GET'])
def get_recent(request):
    """Gets recent articles
    """
    articles = Article.objects.filter(is_visible=True).order_by(
        '-date_created')[:num_articles]
    serializer = ArticleSerializer(articles, many=True)
    return Response({'data': {'articles': serializer.data, 'count': articles.count()}})


@api_view(['GET'])
def get_home(request):
    """Gets homepage articles
    """
    # TODO: Implement better homepage
    articles = Article.objects.filter(is_visible=True).order_by(
        '-date_created')[:num_articles]
    serializer = ArticleSerializer(articles, many=True)
    return Response({'data': {'articles': serializer.data, 'count': articles.count()}})


@api_view(['GET'])
def get_by_id(request, article_id):
    """Gets article by id
    """
    try:
        article = Article.objects.get(Q(is_visible=True) & Q(id=article_id))
        serializer = ArticleSerializer(article)
        return Response({'data': serializer.data})
    except ObjectDoesNotExist:
        return Response('Article not found', status=404)


@api_view(['GET'])
def list_all(request):
    """Lists all articles
    """

    if request.GET.get('amount') != None:
        amount = request.GET.get('amount')
    else:
        amount = 5

    if request.GET.get('offset') != None:
        offset = request.GET.get('offset')
    else:
        offset = 0

    try:
        amount = int(amount)
    except ValueError:
        return Response('amount must be an integer', 400)

    try:
        offset = int(offset)
    except ValueError:
        return Response('offset must be an integer', 400)

    articles = Article.objects.filter(is_visible=True).order_by(
        '-date_created')[offset:offset+amount]
    serializer = ArticleSerializer(articles, many=True)
    return Response({'data': {'articles': serializer.data, 'count': articles.count()}})
