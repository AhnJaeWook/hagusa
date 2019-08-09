from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

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