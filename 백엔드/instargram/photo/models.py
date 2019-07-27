from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to= 'timeline_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    like = models.ManyToManyField(User, related_name = 'like_post', blank=True)
    favorite = models.ManyToManyField(User, related_name='favorite_post', blank=True)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return "text : "+self.text

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('photo:detail', args=[self.id])

class Comment(models.Model):
    post = models.ForeignKey(User, on_delete=models,related_name = 'comments')
    author = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
        
    def __str__(self):
        return "text : "+self.text
        
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