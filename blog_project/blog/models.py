from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
