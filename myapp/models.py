from django.db import models
from django.utils.timezone import now
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    slug = AutoSlugField(populate_from='title', unique_with='sno')
    content = models.TextField()
    author = models.CharField(max_length=25)
    timestamp = models.DateTimeField(default=now,blank=True)
    def __str__(self):
        return 'Post by'+ self.author
    
class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment =models.TextField()
    post =models.ForeignKey(Post,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp =models.DateTimeField(default=now, blank=True)
    def __str__(self):
        return 'Post by'+ self.user.username

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=14)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return 'message by ' + self.name


class Item(models.Model):
    title =models.CharField(max_length=100)
    video = EmbedVideoField()  # same like models.URLField()
