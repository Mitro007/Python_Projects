from django.shortcuts import render
from django.http import HttpResponse

# FBV - always return HttpResponse or Error

def greet(request):
  return HttpResponse('Hello Django!!')

def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')
