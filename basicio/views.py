

from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def login(request):
    return render(request, "login.html")

def profile(request):
    return render(request, "profile.html")

def signup(request):
    return render(request, "signup.html")