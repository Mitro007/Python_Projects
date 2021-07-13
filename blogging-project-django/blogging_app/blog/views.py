from .models import Post
from django.shortcuts import render
from django.http import HttpResponse

# FBV - always return HttpResponse or Error

def greet(request):
  return HttpResponse('Hello Django!!')

def home(request):
  context = {'posts': Post.objects.all(),}
  return render(request, 'home.html', context=context)

def about(request):
  return render(request, 'about.html', {'title': 'About'})
