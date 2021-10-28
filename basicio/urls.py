from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('login', views.login, name="login"),
    path('profile', views.profile, name="profile"),
    path('signup', views.signup, name="signup"),
    path('thanks', views.thanks, name="thanks")
]
