from django.db import models
from django.contrib.auth.models import User


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
    contents_file = models.FileField(upload_to='uploads/')
    header_image = models.ImageField(upload_to='uploads/')
    category = models.ForeignKey(
        Category, related_name='articles', on_delete=models.PROTECT)
    author = models.ForeignKey(
        User, related_name='authored_articles', on_delete=models.PROTECT)
    publisher = models.ForeignKey(
        User, related_name='published_articles', on_delete=models.PROTECT)
    date_created = models.DateField(auto_now_add=True)
    date_edited = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
