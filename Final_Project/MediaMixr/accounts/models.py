from django.db import models
from django.contrib.auth.models import User
import datetime
import sys
sys.path.append("..")
from recommendation.models import Genre

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    primary_interest = models.ForeignKey('Interest', on_delete=models.CASCADE)
    interest_2 = models.ForeignKey('Interest', on_delete=models.CASCADE, related_name='i2')
    interest_3 = models.ForeignKey('Interest', on_delete=models.CASCADE, related_name='i3')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user
    def __str__(self):
        return self.primary_interest
    def __str__(self):
        return self.interest_2
    def __str__(self):
        return self.interest_3
    def __str__(self):
        return self.genre

class Interest(models.Model):
    name = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.name
#
# class Book(models.Model):
#     title = models.CharField(max_length=100, null=False)
#     author = models.CharField(max_length=50, null=False)
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
#
# class Movie(models.Model):
#     title = models.CharField(max_length=100, null=False)
#     studio = models.CharField(max_length=50, null=False)
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
#
# class Video_Game(models.Model):
#     title = models.CharField(max_length=100, null=False)
#     developer = models.CharField(max_length=50, null=False)
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
#
# class TV_Show(models.Model):
#     title = models.CharField(max_length=100, null=False)
#     publisher = models.CharField(max_length=50, null=False)
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Media(models.Model):
    type = models.ForeignKey(Interest, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    creator = models.CharField(max_length=60, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class ForumPost(models.Model):
    title =models.CharField(max_length=60)
    content =models.TextField(null=True)
    pubdate =models.DateTimeField(default=datetime.datetime.today())
    profile =models.ForeignKey(Profile, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)