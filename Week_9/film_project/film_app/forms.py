from django.forms import ModelForm
from django import forms
from .models import *
from django.forms.widgets import SelectDateWidget
from datetime import date


class AddFilm(ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'release_date':SelectDateWidget(years=range(1980, 2020))
        }


class AddDirector(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
