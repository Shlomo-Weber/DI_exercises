from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as django_login, authenticate
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            django_login(request, user)
            return redirect('project/createpost')
        else:
            return render(request, 'registration/login.html')

def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
           new_user= form.save()
           messages.info(request,'Thank you for registering. You are now logged in.')
           new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
           django_login(request=request, user=new_user)
           return redirect('project/createpost')
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})




#
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             messages.info(request, "Thanks for registering. You are now logged in.")
#             new_user = authenticate(username=form.cleaned_data['username'],
#                                     password=form.cleaned_data['password1'],
#                                     )
#             login(request, new_user)
#             return HttpResponseRedirect("/dashboard/")