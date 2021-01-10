from django.db.models import Q
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class UserAdmin(UserAdmin):
    """User admin
    """

    def get_fieldsets(self, request, obj):
        if request.user.is_superuser:
            return super().get_fieldsets(request, obj)
        else:
            if obj:
                # Publisher has full governance over their authors for now
                return (
                    (None, {'fields': [
                     'username', 'is_active', 'first_name', 'last_name']}),
                )
            else:
                return super().get_fieldsets(request, obj)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(profile__created_by=request.user)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        else:
            return []

    def save_model(self, request, obj, form, change):
        super(UserAdmin, self).save_model(request, obj, form, change)
        if not change:
            obj.profile.created_by = request.user
            obj.save()


class ProfileAdmin(admin.ModelAdmin):
    """Profile admin
    """

    def get_fieldsets(self, request, obj):
        if request.user.is_superuser:
            return super().get_fieldsets(request, obj)
        else:
            return (
                (None, {'fields': ['is_author']}),
            )

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(created_by=request.user)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = ['user', 'created_by']
        return readonly_fields


class ArticleAdmin(admin.ModelAdmin):
    """Article admin
    """

    def get_changeform_initial_data(self, request):
        return {'publisher': request.user}

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(publisher=request.user)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'author':
            kwargs["queryset"] = User.objects.filter(
                Q(profile__is_author=True) &
                Q(is_active=True)
            )
        elif db_field.name == 'publisher':
            if request.user.is_superuser:
                kwargs["queryset"] = User.objects.filter(
                    Q(profile__is_publisher=True) &
                    Q(is_active=True)
                )
            else:
                kwargs["queryset"] = User.objects.filter(
                    Q(profile__is_publisher=True) &
                    Q(is_active=True) &
                    Q(id=request.user.id)
                )

        return super(ArticleAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
