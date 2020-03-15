from django.db import models
# Create your models here.

class Animal(models.Model):
    legs = models.IntegerField(default=4)
    weight = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    speed = models.IntegerField(null=True)
    family = models.ForeignKey('Family', on_delete=models.CASCADE)

class Family(models.Model):
    name = models.TextField(null=True)



