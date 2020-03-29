from django.shortcuts import render, redirect
import sys
sys.path.append("..")
from accounts.models import *
from recommendation.models import Genre
import random
# Create your views here.


# def your_recs(request):
#     interest2 = request.user.profile.interest_2
#     interest3 = request.user.profile.interest_3
#     interest_lists = []
#     for interest in [interest2,interest3]:
#         if interest.name == 'Movies':
#             list1 = Media.objects.filter(genre = request.user.profile.genre)
#             interest_lists.append(list1)
#         elif interest.name == 'Books':
#             list1 = Media.objects.filter(genre = request.user.profile.genre)
#             interest_lists.append(list1)
#         elif interest.name == 'TV Shows':
#             list1 = Media.objects.filter(genre = request.user.profile.genre)
#             interest_lists.append(list1)
#     print(interest_lists)
#     return render(request, 'recommendation/your_recs.html',{'interest2': interest_lists[0], 'interest3': interest_lists[1]})

def your_recs(request):
    profile = request.user.profile
    media_list_1 = Media.objects.filter(genre=profile.genre, type=profile.interest_2)
    media_list_2 = Media.objects.filter(genre=profile.genre, type= profile.interest_3)

    return render(request, 'recommendation/your_recs.html', {'media_list_1':media_list_1, 'media_list_2':media_list_2})

def primary_recs(request):
    profile = request.user.profile
    primary_media = Media.objects.filter(genre = profile.genre, type = profile.primary_interest)
    return render(request, 'recommendation/primary_recs.html', {'primary_media':primary_media})

def all_media(request):
    all_media = Media.objects.all()

    return render(request, 'recommendation/all_media.html', {'all_media':all_media})

def show_interest(request, interest_id):
    interests = Media.objects.filter(type__id=interest_id)

    return render(request, 'recommendation/show_interests.html', {'interests':interests})

def surprise_me(request):
    random_media = random.choices(Media.objects.all(), k=6)
    return render(request, 'recommendation/show_interests.html', {'interests':random_media, 'surprise':True})

def show_genre(request, genre_id):
    genres = Media.objects.filter(genre__id=genre_id)
    return render(request, 'recommendation/show_genres.html', {'genres':genres})

def all_genres(request):
    all_genres = Genre.objects.all()

    return render(request, 'recommendation/all_genres.html', {'all_genres':all_genres})