####################################################################################################
# Burasi main/settings.py bölgesi

import os

INSTALLED_APPS = [
    ...
    # 3. parti appler,
    'crispy_forms',
    # benim applerim
    'kullaniciapp',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi media/profile_pics/ bölgesi

####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullanicilarapp/models.py bölgesi

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    portfolio=models.URLField(blank=True)
    # URLField sadece url'lerin girilmesine izin verir.
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # Django'nun bize sundugu formu yeterli bulmadigimiz icin sekilde baska propertyler ekleyerek kendi tablomuzu olusturduk.
    # Daha sonra Django'nun kendi formuyla aralarinda one to one iliski kurduk. Böylece index numaralari eslesmis oldu.

    def __str__(self):
        return self.user.username
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi kullanicilarapp/admin.py bölgesi

from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullanicilarapp/forms.py bölgesi

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserForm(UserCreationForm):
    class Meta():
        model=User
        fields=('username','email')

class UserProfileForm(forms.ModelForm):
    class Meta():
       model=UserProfile
       exclude=('user',)
       # user haricindeki tüm field'leri getir.
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi kullanicilarapp/views.py bölgesi

from multiprocessing import context
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from kullanicilarapp.forms import UserForm, UserProfileForm

def home(request):
    return render(request, 'kullanicilarapp/home.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    form_user=UserForm()
    form_profile=UserProfileForm()
    if request.method=='POST':
        form_user=UserForm(request.POST)
        form_profile=UserProfileForm(request.POST,request.FILES)
        if form_user.is_valid() and form_profile.is_valid():
            user=form_user.save()
            profile=form_profile.save(commit=False) # bunu olustur, ama kaydetme.
            profile.user=user # benim profile tablomun user alani user tablosunda. 
            profile.save()
            login(request,user)
            messages.success(request,'Register Successfull')
            return redirect('home')
    context={
        'form_profile':form_profile,
        'form_user':form_user
    }
    return render(request,'kullanicilarapp/register.html',context)

def user_login(request):
    form=AuthenticationForm(request,data=request.POST)
    if form.is_valid():
        user=form.get_user()
        login(request,user)
        messages.success(request,'login successful')
        return redirect('home')

    return render(request,'kullanicilarapp/user_login.html',{'form':form})
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullanicilarapp/urls.py bölgesi

from django.urls import path
from .views import register, user_logout, user_login

urlpatterns = [
    path('register/', register, name='register' ),
    path('logout/', user_logout, name='logout' ),
    path('login/', user_login, name='user_login'),
]
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi main/urls.py bölgesi

from django.contrib import admin
from django.urls import path, include
from users.views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('users/', include('users.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullanicilarapp/templates/kullanicilarapp/base.html bölgesi

<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css"
        integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous" />
    {% comment %}
    <link rel="stylesheet" href=" {% static 'kullanicilarapp/css/bootstrap.min.css' %}" />
    {% endcomment %}
    <link rel="stylesheet" href=" {% static 'kullanicilarapp/css/style.css' %}  " />
    <title>Document</title>
</head>
<body>
    {% include "kullanicilarapp/navbar.html" %}
    <div style="margin-top: 100px; margin-bottom: 100px" class="container">
        {% if messages %}
        {% for message in messages %}
        {% if message.tags == "error" %}
        <div class="alert alert-danger">{{ message }}</div>
        {% else %}
        <div class="alert alert-{{ message.tags }}">{{ message }}</div>
        {% endif %}
        {% endfor %}
        {% endif %}
        {% block content %}
        {% endblock content %}
    </div>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous">
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous">
    </script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous">
    </script>
    <script src="{% static 'users/js/timeout.js' %}"></script>
</body>
</html>
####################################################################################################
#
#
#
#
#
#
####################################################################################################
# Burasi kullaniciapp/templates/kullaniciapp/home.html bölgesi

{% extends 'kullanicilarapp/base.html' %} {% block content %}
<h1>Home Page</h1>
{% if request.user.is_authenticated %}
<h2>Wellcome {{request.user}}!</h2>
{% else %}
<h2 id="welcome">Wellcome Guest!</h2>
{% endif %} {% endblock content %}
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullaniciapp/templates/kullaniciapp/register.html bölgesi

{% extends 'kullanicilarapp/base.html' %} {% block content %} {% load crispy_forms_tags %}

<h2>Registration Form</h2>

{% if request.user.is_authenticated %}

<h3>Thanks for registering</h3>

{% else %}

<h3>Fill out the form please!</h3>
<form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %} {{ form_user | crispy }}
    <button type="submit" class="btn btn-danger">Register</button>
</form>
{% endif %} {% endblock content %}
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullaniciapp/templates/kullaniciapp/login.html bölgesi

{% extends 'kullanicilarapp/base.html' %} {% block content %} {% load crispy_forms_tags %}
<div class="row">
    <div class="col-md-6 offset-md-3">
        <h3>Please Login</h3>
        <form action="{% url 'user_login' %}" method="post">
            {% csrf_token %} {{form|crispy}}
            <button type="submit" class="btn btn-danger">Login</button>
        </form>
    </div>
</div>
{% endblock content %}
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullaniciapp/templates/kullaniciapp/navbar.html bölgesi

{% load static %}

<nav class="navbar navbar-toggleable-md navbar-inverse fixed-top bg-inverse">
  <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarCollapse"
    aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <a class="navbar-brand" href="{% url 'home'  %}"><img src="{% static 'users/images/cw_logo.jpg' %}"
      alt="CLARUSWAY_LOGO" />

    Clarusway FS</a>

  <div class="collapse navbar-collapse" id="navbarCollapse">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        {% comment %} {% url 'students' %} {% endcomment %}
        <a class="nav-link" href="">Students</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="">Contact</a>
      </li>
    </ul>

    <ul class="navbar-nav ml-auto">
      {% if request.user.is_authenticated %} {% if request.user.is_superuser %}

      <li class="nav-item active">
        <a class="nav-link" href="/admin">Admin</a>
      </li>
      {% endif %}

      <li class="nav-item active">
        {% comment %} {% url 'logout' %} {% endcomment %}
        <a class="nav-link" href="{% url 'logout' %}">Log Out</a>
      </li>
      {% else %}

      <li class="nav-item active">
        {% comment %} {% url 'user_login' %} {% endcomment %}
        <a class="nav-link" href="{% url 'user_login' %}">Log In</a>
      </li>
      {% endif %}
      <li class="nav-item active">
        {% comment %} {% url 'register' %} {% endcomment %}
        <a class="nav-link" href="{% url 'register' %}">Register</a>
      </li>
    </ul>
  </div>
</nav>
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullanicilarapp/static/kullaniciapp/js/timeout.js bölgesi

let element = document.querySelector(".alert");
let element2 = document.querySelector("#welcome");

element &&
  setTimeout(function () {
    element.style.display = "none";
  }, 3000);

element2 &&
  setTimeout(function () {
    element2.style.display = "none";
  }, 3000);
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullaniciapp/static/kullaniciapp/images/ bölgesi

# cw_logo.jpg
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullaniciapp/static/kullaniciapp/css/bootstrap.min.css bölgesi

# bazi css kodlari
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullaniciapp/static/kullaniciapp/css/style.css bölgesi

h1 {
  background-color: red;
}
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi main/settings.py bölgesi

import os

INSTALLED_APPS = [
    ...
    # 3. parti appler,
    'crispy_forms',
    # benim applerim
    'kullaniciapp',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
####################################################################################################
