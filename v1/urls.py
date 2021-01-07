from v1.views import admin
from django.urls import path
from .views import admin, authors, articles, categories, staff

urlpatterns = [
    path('admin/auth/', admin.check_auth),
    path('admin/create-user/', admin.create_user),
    path('admin/delete-article/', admin.delete_article),

    path('articles/count/', articles.get_count),
    path('articles/search/', articles.search),
    path('articles/recent/', articles.get_recent),
    path('articles/home/', articles.get_home),
    path('articles/category/<int:category_id>/', articles.get_by_category),
    path('articles/<int:article_id>/', articles.get_by_id),
    path('articles/', articles.list_all),

    path('authors/', authors.list_all),

    path('categories/', categories.list_all),
    path('categories/<int:category_id>/', categories.get_by_id),

    path('staff/auth/', staff.check_auth),
    path('staff/create-author/', staff.create_author),
    path('staff/publish-article/', staff.publish_article),
]
