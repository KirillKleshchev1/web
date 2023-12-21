from django.shortcuts import render
from django.urls import path
from django.views import home
urlpatterns = [path('', home, name='home')]

def home(request):
    return render(request, 'index.html')

input()