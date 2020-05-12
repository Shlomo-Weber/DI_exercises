from .models import *
from django.forms import ModelForm
from django.forms import *


class ForumPostForm(ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content','media']

class ForumMediaPostForm(ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content',]

class ForumCommentForm(ModelForm):
    class Meta:
        model = ForumComment
        fields = ['content']