# Generated by Django 2.1.7 on 2019-08-05 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.AddField(
            model_name='comment',
            name='Photo',
            field=models.ForeignKey(null=True, on_delete=True, to='photo.Photo'),
        ),
    ]
