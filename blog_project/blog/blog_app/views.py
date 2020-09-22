from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    """ Displays the home page consisting all posts """
    posts = Post.objects.all()
    return render(request, 'blog_app/home.html', {'posts': posts})


def about(request):
    """ Displays profile information """
    return render(request, 'blog_app/about.html', {'title': 'About'})