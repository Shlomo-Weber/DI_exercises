from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.

def index(request):

    return render(request, 'film_app/index.html')

def homepage(request):

    return render(request, 'film_app/homepage.html')

def add_film(request):
    if request.method == 'POST':
        form = AddFilm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = AddFilm()
    return render(request, 'film_app/addfilm.html', {'form':form})


def add_director(request):
    if request.method == 'POST':
        form = AddDirector(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = AddDirector()
    return render(request, 'film_app/add_director.html', {'form': form, })


def allfilms(request):

    films = Film.objects.all()
    directors = Director.objects.all()

    return render(request, 'film_app/allfilms.html', {'films':films,'directors': directors})

def edit_director(request, director_id):
    director = Director.objects.get(pk=director_id)
    if request.method == 'POST':
        form = AddDirector(request.POST,instance=director)
        if form.is_valid():
            form.save()
        return redirect('allfilms')
    form = AddDirector(instance=director)
    return render(request, 'film_app/add_director.html', {'form': form, 'btn_text':'Edit'})

