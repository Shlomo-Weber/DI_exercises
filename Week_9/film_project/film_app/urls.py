from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
path('', index, name='index'),
path('home/', homepage, name='home'),
path('add_film/', add_film, name='addfilm'),
path('add_director/', add_director, name='adddirector'),
path('allfilms/', allfilms, name='allfilms'),
path('edit_director/<int:director_id>', edit_director, name='edit_director')

    ]