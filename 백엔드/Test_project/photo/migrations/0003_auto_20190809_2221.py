# Generated by Django 2.2.3 on 2019-08-09 13:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0002_auto_20190809_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='like3',
            field=models.ManyToManyField(blank=True, related_name='like3_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='like4',
            field=models.ManyToManyField(blank=True, related_name='like4_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='like5',
            field=models.ManyToManyField(blank=True, related_name='like5_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
