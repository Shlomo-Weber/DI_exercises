from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=80)
    content = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title
    def __int__(self):
        return self.id


class Comment(models.Model):
    content = models.TextField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Post name {self.post}, Comment id {self.id}'
    def __int__(self):
        return self.id

