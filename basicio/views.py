
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignUpForm, LoginForm, CreateHubForm
from basicio.models import User, Hubuser, Hub
from datetime import datetime


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def hub(request, slug):
    print(request.COOKIES['user'])
    return render(request, "hub.html", {"hubName":slug})

def createHub(request):
    if request.method == "POST":
        form = CreateHubForm(request.POST)
        if form.is_valid():
            hubName = form.cleaned_data["hubname"]
            if Hub.objects.filter(hubname=hubName).count() > 0:
                return render(request, "create_hub.html", {"form":createHubForm, "error_message":"The Hub Name already Exists"})
            else:
                hubDesc = form.cleaned_data["hubdesc"]
                creator = request.COOKIES['user']
                hub = Hub()
                hub.hubname = hubName
                hub.hubdesc = hubDesc
                hub.creator = creator
                hub.save()
                return redirect("/thanks")
    else:
        form = CreateHubForm()
        return render(request, "create_hub.html", {"form":form})

# Not yet implemented link change
def profile(request):
    # .POST.iterlists()
    # data = dict(request.POST)
    # print(profile["uname"])
    # print(profile["password"])

    data = request.COOKIES['user']
    hubUsers = Hubuser.objects.select_related('userid', 'hubid')
    hubs = [hub.hubid.hubname for hub in hubUsers if hub.userid.username == data]
    print(hubs)
    # return render(request, "profile.html", {"username":data["uname"][0]})
    return render(request, "profile.html", {"username":data, "hubs":hubs})

def thanks(request):
    return render(request, "thanks.html")

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["uname"]
            password = form.cleaned_data["password"]

            user_obj = User.objects.get(username=username, passwd=password)
            if user_obj:
                print("Thanks for logging in")
                # request.COOKIES['user'] = username
                # request.set_cookie('user', username)
                profile_redirect = HttpResponseRedirect("/profile")
                profile_redirect.set_cookie("user", username)
                return profile_redirect
            else:
                return render(request, "login.html", {"form":form, "error_message":"Incorrect Username or Password"})
    else:
        form = LoginForm()
        return render(request, "login.html", {"form":form})

def signup(request):
    print(request.headers)
    if request.method == "POST":
        form = SignUpForm(request.POST)
        print("here")
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data["uname"]).count() > 0:
                print(form.cleaned_data["uname"])
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
