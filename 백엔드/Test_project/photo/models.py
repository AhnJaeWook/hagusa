from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model
from django.utils import timezone
from django import forms
from django.conf import settings
# Create your models here.

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='timeline_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    like1 = models.ManyToManyField(User, related_name='like1_post', blank=True)
    like2 = models.ManyToManyField(User, related_name='like2_post', blank=True)
    like3 = models.ManyToManyField(User, related_name='like3_post', blank=True)
    like4 = models.ManyToManyField(User, related_name='like4_post', blank=True)
    like5 = models.ManyToManyField(User, related_name='like5_post', blank=True)

    def __str__(self):
        return "text : " + self.text

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('photo:detail',args=(self.id))


class Comment(models.Model):
    photo = models.ForeignKey(Photo,on_delete=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=True, null=True)
    comment_date = models.DateTimeField(default=timezone.now)
    comment_text = models.TextField()
    
    class Meta:
        ordering = ['comment_date'] #id역순으로 정렬이에용
    
    def get_edit_url(self):
        return reverse('comment_edit', args=[self.photo.pk,  self.pk])

    def get_delete_url(self):
        return reverse('comment_delete', args=[self.photo.pk,  self.pk])