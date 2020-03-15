from django.db import models
from datetime import date
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'
class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(default=date.today())
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    director = models.OneToOneField('Director', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f'{self.title}'

class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        fullname = f'{self.first_name} {self.last_name}'
        return f'{fullname}'

    def getfullname(self):
        return f'{self.first_name} {self.last_name}'



