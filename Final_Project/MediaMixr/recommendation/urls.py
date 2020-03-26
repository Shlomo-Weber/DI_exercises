from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', your_recs, name='your_recs'),
    # path('suprise_me/', surprise_me, name='suprise_me'),
    # path('books/', books, name='books'),
    # path('movies/', movies, name='movies'),
    # path('tv_shows/', tv_shows, name='tv_shows'),
    # path('v_games/', v_games, name='v_games')
]