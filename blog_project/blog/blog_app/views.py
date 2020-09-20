from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'Harsh Biyani',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 19, 2020'
    },
    {
        'author': 'Harshita Biyani',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 20, 2020'
    },
]

def home(request):
    """ Displays the home page consisting all posts """
    context = {'posts': posts}
    return render(request, 'blog_app/home.html', context=context)


def about(request):
    """ Displays profile information """
    return render(request, 'blog_app/about.html', {'title': 'About'})