from django.http import JsonResponse
from django.shortcuts import render, redirect
import sys
sys.path.append("..")
from accounts.forms import GenreForm
from accounts.models import *
from recommendation.models import Genre
from recommendation.forms import Recommend_MediaForm
import random
from django.contrib import messages
# Create your views here.

def your_recs(request):
    profile = request.user.profile
    media_list_1 = Media.objects.filter(genre=profile.genre, type=profile.interest_2)
    media_list_2 = Media.objects.filter(genre=profile.genre, type= profile.interest_3)
    form = GenreForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            profile.genre = form.cleaned_data['genre']
            profile.save()
            return redirect('your_recs')
    else:
        form = GenreForm()
    return render(request, 'recommendation/your_recs.html', {'media_list_1':media_list_1, 'media_list_2':media_list_2, 'form':form})

def primary_recs(request):
    profile = request.user.profile
    primary_media = Media.objects.filter(genre = profile.genre, type = profile.primary_interest)
    form = GenreForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            profile.genre = form.cleaned_data['genre']
            profile.save()
            return redirect('primary_recs')
    else:
        form = GenreForm()
    return render(request, 'recommendation/primary_recs.html', {'primary_media':primary_media, 'form':form})

def all_media(request):
    all_media = Media.objects.all()
    page_h1 = 'This is all our media'
    if request.method=='POST':
        media_title = request.POST.get('media')
        all_media=Media.objects.filter(title=media_title)
    return render(request, 'recommendation/show_interests.html', {'all_media':all_media, 'page_h1':page_h1, 'everything':True})

def show_interest(request, interest_id):
    interests = Media.objects.filter(type__id=interest_id)
    page_h1 = interests[0].type.name
    return render(request, 'recommendation/show_interests.html', {'all_media':interests, 'page_h1':page_h1})

def surprise_me(request):
    random_media = random.choices(Media.objects.all(), k=6)
    return render(request, 'recommendation/show_interests.html', {'all_media':random_media, 'surprise':True})

def show_genre(request, genre_id):
    genres = Media.objects.filter(genre__id=genre_id)
    page_h1 = genres[0].genre.name
    return render(request, 'recommendation/show_interests.html', {'all_media':genres, 'page_h1':page_h1})

def all_genres(request):
    all_genres = Genre.objects.all()

    return render(request, 'recommendation/all_genres.html', {'all_genres':all_genres})

def recommend_media(request):
    if request.method == 'POST':
        form = Recommend_MediaForm(request.POST)
        if form.is_valid():
            new_media = form.save()
            messages.success(request, 'Thank you! Your recommendation is pending approval by our admins.')
            return redirect('rec_media')
    else:
        form = Recommend_MediaForm()
    return render(request, 'recommendation/rec_media.html', {'form':form})
