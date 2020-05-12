from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
import sys
sys.path.append("..")
from accounts.models import Media
# Create your views here.

def forum_main(request):
    posts = ForumPost.objects.all()
    # comments = ForumComment.objects.all()
    if request.method == 'POST':
        form = ForumCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            post_id = request.POST['post']
            post = ForumPost.objects.get(pk=post_id)
            print(request.POST)
            comment.post = post
            comment.profile = request.user.profile
            comment.save()
            return redirect('forum_home')
    else:
        form = ForumCommentForm()
    return render(request, 'forum/forum_home.html', {'posts': posts, 'form':form})

def create_post(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        post = form.save(commit=False)
        post.profile = request.user.profile
        messages.success(request,'Post created successfully')
        post.save()
        return redirect('forum_home')
    else:
        form = ForumPostForm()
        return render(request, 'forum/create_post.html',{'form':form})

def create_mediapost(request, media_id):
    media = Media.objects.get(id=media_id)
    if request.method == 'POST':
        form = ForumMediaPostForm(request.POST)
        post = form.save(commit=False)
        post.profile = request.user.profile
        post.media = media
        messages.success(request,'Post created successfully')
        post.save()
        return redirect('forum_home')
    else:
        form = ForumMediaPostForm()
        return render(request, 'forum/create_post.html',{'form':form})