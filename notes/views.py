from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return  render(request,'notes/index.html')


def register(request):
    return render(request,'notes/register.html')

def login(request):
    return render(request,'notes/login.html')

def home_page(request):
    return render(request,'notes/home.html')

def settings(request):
    return render(request,'notes/settings.html')

def loggedout(request):
    return render(request,'notes/loggedout.html')

def update(request):
    return render(request,'notes/update.html')

