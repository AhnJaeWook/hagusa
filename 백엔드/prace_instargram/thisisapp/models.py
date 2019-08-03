from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()


    def __str__(self):
        return self.title
    
#이 친구는 주소값을 쉽게해주는거 comment.blog로
    def get_absoulute_url(self):
        return reverse('detail', args=[self.pk])

    def summary(self):
        return self.body[:50]
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=True, null=True)
    comment_date = models.DateTimeField(default=timezone.now)
    comment_text = models.TextField()
    
    class Meta:
        ordering = ['-comment_date'] #id역순으로 정렬이에용

    def get_edit_url(self):
        return reverse('comment_edit', args=[self.blog.pk,  self.pk])

    def get_delete_url(self):
        return reverse('comment_delete', args=[self.blog.pk,  self.pk])