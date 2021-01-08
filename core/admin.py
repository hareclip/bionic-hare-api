from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'author':
            kwargs["queryset"] = User.objects.filter(
                profile__is_author=True,
            )
        elif db_field.name == 'publisher':
            kwargs["queryset"] = User.objects.filter(
                profile__is_publisher=True,
            )
        return super(ArticleAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
