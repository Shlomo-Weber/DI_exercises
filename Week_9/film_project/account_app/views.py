from django.shortcuts import render, redirect,reverse
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages

from django.contrib.auth import authenticate,logout as dlogout,login as dlogin
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username = form.cleaned_data['username']).exists():
                messages.warning(request, f'{form.cleaned_data["username"]} is already in use')
                return redirect ('signup')
            user= User.objects.create_user(**form.cleaned_data)
        return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'account_app/signup.html', {'form':form})


def login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            dlogin(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'account_app/login.html', {'form':form})


def logout(request):
    dlogout(request)
    return redirect('index')


def profile(request, user_pk):
    currentuser = User.objects.get(id=user_pk)

    return render(request, 'account_app/profile.html', {'currentuser':currentuser})