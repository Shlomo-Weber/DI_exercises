from django.shortcuts import render, redirect
from django.contrib.auth import login as dlogin, logout as dlogout, authenticate
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def home(request):

    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, f'New User Created: Welcome {username}')
            dlogin(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            messages.success(request, "You are now logged in!")
            dlogin(request, user)
        else:
            return render(request, 'registration/login.html')

@login_required
def profile(request):
    if request.method =="POST":
        form = ProfileForm(request.POST)
        if form.is_valid() and 'create' in request.POST:
            interests = form.save(commit=False)
            interests.user = request.user
            interests.save()
            return redirect('your_recs')
        elif form.is_valid() and 'update' in request.POST:
            profile = request.user.profile
            profile.primary_interest = form.cleaned_data['primary_interest']
            profile.interest_2 = form.cleaned_data['interest_2']
            profile.interest_3 = form.cleaned_data['interest_3']
            profile.genre = form.cleaned_data['genre']
            profile.save()
    else:
        form = ProfileForm()
    return render(request, 'accounts/profile.html', {'form':form})

def logout(request):

    return render(request, 'accounts/home.html')

