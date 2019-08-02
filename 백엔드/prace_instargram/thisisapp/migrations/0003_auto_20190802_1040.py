# Generated by Django 2.1.7 on 2019-08-02 01:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thisisapp', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_user',
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
