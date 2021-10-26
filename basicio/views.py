

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignUpForm

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def login(request):
    return render(request, "login.html")

def profile(request):
    return render(request, "profile.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SignUpForm()

    return render(request, "signup.html", {'form':form})
