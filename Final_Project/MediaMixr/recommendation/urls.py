from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', your_recs, name='your_recs'),
    path('primary/', primary_recs, name = 'primary_recs'),
    path('allmedia/', all_media, name='all_media'),
    path('surprise_me/', surprise_me, name='surprise_me'),
    path('interest/<int:interest_id>', show_interest, name='show_interests'),
    path('genre/<int:genre_id>', show_genre, name='show_genres'),
    path('allgenres/', all_genres, name='all_genres'),
    path('rec_media/', recommend_media, name='rec_media')
]