from django.forms import ModelForm
from django import forms
from .models import Post

class CreatePost(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
