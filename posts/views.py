from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.forms.fields import ImageField
from django import forms

# Create your views here.

def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())



    # get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    form=PostForm()
    

    # show
    return render(request, 'posts.html',
                    {'posts': posts})


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

# I dont understand how to build this..

def edit(request, id):
    if request.method == "GET": 
        posts = Post.objects.get(id = id)
        return render(request, "edit.html", {"posts": posts})
    if request.method == "POST":
        editposts = Post.objects.get(id = id)
        form = PostForm(request.POST, request.FILES, instance= editposts)
        if form.is_valid ():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("not valid")


def like(request, post_id):
    print(post_id)
    liketweet = Post.objects.get(id = post_id)
    liketweet.like += 1
    liketweet.save()
    return HttpResponseRedirect("/")

