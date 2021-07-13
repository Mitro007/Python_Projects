from django.shortcuts import render
from django.http import HttpResponse

# FBV - always return HttpResponse or Error

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def greet(request):
  return HttpResponse('Hello Django!!')

def home(request):
  context = {'posts': posts,}
  return render(request, 'home.html', context=context)

def about(request):
  return render(request, 'about.html', {'title': 'About'})
