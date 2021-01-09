import os
import uuid
import magic
from django.core.exceptions import ValidationError
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@deconstructible
class FileValidator():
    """
    Factory to validates file field with magic
    https://stackoverflow.com/questions/3648421/only-accept-a-certain-file-type-in-filefield-server-side
    """

    def __init__(self, valid_mime_types=[], valid_file_extensions=[]):
        self.valid_mime_types = valid_mime_types
        self.valid_file_extensions = valid_file_extensions

    def __call__(self, file):
        file_mime_type = magic.from_buffer(file.read(1024), mime=True)
        if file_mime_type not in self.valid_mime_types:
            raise ValidationError('Unsupported file type.')

        ext = os.path.splitext(file.name)[1]
        if ext.lower() not in self.valid_file_extensions:
            raise ValidationError('Unacceptable file extension.')


class Profile(models.Model):
    """User profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_author = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, null=True, blank=True, related_name='created_profiles', on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        instance.profile = Profile.objects.create(user=instance)


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
    contents_file = models.FileField(
        upload_to=RenameFile('res/articles/'),
        validators=[FileValidator(
            ['text/markdown', 'text/plain'],
            ['.md'],
        )],
    )
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
