# Generated by Django 3.1.5 on 2021-01-07 22:40

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_auto_20210107_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_author', models.BooleanField(default=False)),
                ('is_publisher', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_profiles', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='contents_file',
            field=models.FileField(upload_to=core.models.RenameFile('res/articles/')),
        ),
        migrations.AlterField(
            model_name='article',
            name='header_image',
            field=models.ImageField(upload_to=core.models.RenameFile('res/images/')),
        ),
        migrations.DeleteModel(
            name='AuthorProfile',
        ),
    ]