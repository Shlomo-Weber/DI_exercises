from django.shortcuts import render, redirect
import sys
sys.path.append("..")
from accounts.models import *
# Create your views here.


def your_recs(request):
    # interest2 = request.user.profile.interest_2
    # interest3 = request.user.profile.interest_3
    # interest_lists = []
    # for interest in [interest2,interest3]:
    #     if interest.name == 'Movies':
    #         list1 = Movie.objects.filter(genre = request.user.profile.genre)
    #         interest_lists.append(list1)
    #     elif interest.name == 'Books':
    #         list1 = Book.objects.filter(genre = request.user.profile.genre)
    #         interest_lists.append(list1)
    #     elif interest.name == 'TV Shows':
    #         list1 = TV_Show.objects.filter(genre = request.user.profile.genre)
    #         interest_lists.append(list1)
    # {'interest2': interest_lists[0], 'interest3': interest_lists[1]})
    return render(request, 'recommendation/your_recs.html')