from django.db import models
import sys
sys.path.append("..")
from accounts.models import *
# Create your models here.

class ForumPost(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(null=True)
    pubdate = models.DateTimeField(default=datetime.datetime.today())
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
