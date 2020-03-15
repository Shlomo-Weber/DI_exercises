from django.shortcuts import render

# Create your views here.

def index(request):


    return render(request, 'index.html')

def info(request):
    animals = ['Mammal', 'Reptile', 'Insect', 'Arachnid', 'Amphibian', 'Marsupial']
    return render(request, 'info.html', {"animals":animals})