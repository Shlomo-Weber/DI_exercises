from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
path('', forum_main, name='forum_home'),
path('cp/',create_post, name='create_post'),
path('cp/<int:media_id>', create_mediapost, name='create_mediapost')
]