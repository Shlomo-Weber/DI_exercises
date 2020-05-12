from django.db import models
import sys
sys.path.append("..")
from accounts.models import *
import datetime
# Create your models here.

class ForumPost(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(null=True)
    pubdate = models.DateTimeField(default=datetime.datetime.now())
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)

    def __str__(self):
        return f'Post: {self.title}'

    def __str__(self):
        return f'Profile:{self.profile}'


class ForumComment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)