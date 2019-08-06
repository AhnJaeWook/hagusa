from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
from django.utils import timezone
from django import forms
from django.conf import settings

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to= 'timeline_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    like = models.ManyToManyField(User, related_name = 'like_post', blank=True)
    favorite = models.ManyToManyField(User, related_name='favorite_post', blank=True)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return "text : "+self.text


    def get_absolute_url(self):
        return reverse('photo:detail', args=[self.id])



class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("data published")
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return str(self.body)[:100]

    def pretty_pub_date(self):
        return self.pub_date.strftime("%y.%m.%d")

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