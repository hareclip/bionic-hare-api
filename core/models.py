import os
import uuid
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible


@deconstructible
class RenameFile():
    """File renamer factory
    """

    def __init__(self, upload_to):
        self.upload_to = upload_to

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # Set new file name
        if instance.id:
            filename = '{}.{}'.format(instance.id, ext)
        else:
            filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        return os.path.join(self.upload_to, filename)


class AuthorProfile(models.Model):
    """Author profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name='created_author_profiles', on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.user.username


class Category(models.Model):
    """Article category
    """
    label = models.CharField(max_length=300)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = "categories"


class Article(models.Model):
    """Article model
    """
    title = models.CharField(max_length=300)
    contents_file = models.FileField(upload_to=RenameFile('res/articles/'))
    header_image = models.ImageField(upload_to=RenameFile('res/images/'))
    category = models.ForeignKey(
        Category, related_name='articles', on_delete=models.PROTECT)
    author = models.ForeignKey(
        User, related_name='authored_articles', on_delete=models.PROTECT)
    publisher = models.ForeignKey(
        User, related_name='published_articles', on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
