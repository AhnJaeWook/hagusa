from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]
        