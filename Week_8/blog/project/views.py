from django.shortcuts import render, redirect
from project.models import Post
from project.forms import CreatePost

# Create your views here.

def home(request):

    return render(request, 'home.html')


def allposts(request):
    allposts = Post.objects.all()

    return render(request, 'allposts.html', {'allposts': allposts})

def create_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        post = form.save(commit=False)
        post.user = request.user
        post.save()

        return redirect('allposts')

    form = CreatePost()
    return render(request, 'create_post.html', {'form': form})

