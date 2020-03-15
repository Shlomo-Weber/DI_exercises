from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('allposts/', allposts, name='allposts'),
    path('createpost', create_post, name='create_post')

]