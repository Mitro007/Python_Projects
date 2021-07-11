from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.greet, name='blog-greet'),
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]