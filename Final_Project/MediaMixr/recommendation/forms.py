from django import forms
from django.forms import ModelForm
from django.forms.widgets import *
import sys
sys.path.append("..")
from accounts.models import Media


class Recommend_MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = '__all__'
        exclude = ['approved']


