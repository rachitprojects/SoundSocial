

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from basicio.models import User
from datetime import datetime


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def profile(request):
    return render(request, "profile.html")

def thanks(request):
    return render(request, "thanks.html")

def login(request):
    form = LoginForm()
    return render(request, "login.html", {"form":form})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data["uname"]).count() > 0:
                print(form.cleaned_data["uname"])
                print("here")
                return render(request, "signup.html", {'form':form, 'error_message':"Username Exists"})
            else:
                temp_user = User()
                temp_user.username = form.cleaned_data["uname"]
                temp_user.firstname = form.cleaned_data["first_name"]
                temp_user.lastname = form.cleaned_data["last_name"]
                temp_user.passwd = form.cleaned_data["password"]
                temp_user.gender = form.cleaned_data["gender"]
                temp_user.dob = form.cleaned_data["birth_date"].strftime("%Y-%m-%d")
                temp_user.emailid = form.cleaned_data["emailId"]
                temp_user.timeofjoin = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                temp_user.save()
                return redirect('thanks')
    else:
        form = SignUpForm()
        return render(request, "signup.html", {'form':form})
