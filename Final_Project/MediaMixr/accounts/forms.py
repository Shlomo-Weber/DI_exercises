from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms.widgets import *
from .models import Interest
import sys
sys.path.append("..")
from recommendation.models import Genre

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )

class ProfileForm(forms.ModelForm):
    primary_interest = forms.ModelChoiceField(queryset=Interest.objects.all(), label= 'What would you say is your primary media form?')
    interest_2 = forms.ModelChoiceField(queryset=Interest.objects.all(), label="Please choose the media form you're most interested in (NOT YOUR PRIMARY)")
    interest_3 = forms.ModelChoiceField(queryset=Interest.objects.all(), label="Please choose another media form you're interested in")
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), label='Please choose your preferred genre')
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'primary_interest': Select(attrs={'class': 'select'}),
            'interest_2': Select(attrs={'class': 'select'}),
            'interest_3': Select(attrs={'class': 'select'}),
            'genre': Select(attrs={'class': 'select'})
        }
class GenreForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['genre']