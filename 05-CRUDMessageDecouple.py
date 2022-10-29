####################################################################################################
# Burasi ogrenciapp/templates/ogrenciapp/base.html bölgesi

<!DOCTYPE html>
{% load static %}

<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css"
      integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ"
      crossorigin="anonymous"
    />

    {% comment %}
    <link rel="stylesheet" href=" {% static 'fscohort/css/bootstrap.min.css' %}" />
    {% endcomment %}

    <link rel="stylesheet" href=" {% static 'fscohort/css/style.css' %}  " />

    <title>Document</title>
  </head>

  <body>
    <h1> hello clarusway </h1>
    {% comment %} {% include "users/navbar.html" %} {% endcomment %}
    <div style="margin-top: 100px; margin-bottom: 100px" class="container">

      {% block container %}{% endblock container %}
    </div>
    <script
      src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"
    ></script>
    <script src="{% static 'fscohort/js/timeout.js' %}"></script>
  </body>
</html>
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi ogrenciapp/templates/ogrenciapp/index.html bölgesi

{% extends "fscohort/base.html" %} {% block container %}

<h1>Home Page</h1>

<h3>Student App</h3>

{% endblock container %}
####################################################################################################
#
#
#
#
#####################################################################################################
# Burasi ögrenciapp/templates/ögrenciapp/ogrenci_listesi.html bölgesi

{% extends "fscohort/base.html" %}

{% block container %}
    <!-- {{student}} -->
    <ul>
        {% for student in students%}
        <a href="{% url 'detail' student.id  %}">
        <li>{{ student.number }} - {{student.first_name}} {{student.last_name}}</li>
        <a>
        {%endfor%}
    </ul>
{% endblock container %}
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi ögrenciapp/templates/ögrenciapp/ogrenci_ekle.html bölgesi

{% extends 'fscohort/base.html' %}

{% block container %}
    <h2>Add Student</h2>
    <form action="" method="POST">
        {% csrf_token %}                   
        {{form.as_p}}						   
        <input type="submit" value="add">
    </form>
{% endblock container %}
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi ögrenciapp/templates/ögrenciapp/ogrenci_guncelle.html bölgesi

{% extends 'fscohort/base.html' %}

{% block container %}
    <h2>Update Student</h2>
    <form action="" method="POST">
        {% csrf_token %}                   
        {{form.as_p}}						   
        <input type="submit" value="update">
    </form>
{% endblock container %}
####################################################################################################
#
#
#
#
#####################################################################################################
# Burasi ögrenciapp/templates/ögrenciapp/ogrenci_sil.html bölgesi

{% extends 'fscohort/base.html' %}

{% block container %}
    <form action="" method="POST">
        <p>Are You Sure! {{ student }}</p>
        {% csrf_token %}
        <input type="submit" value="Yes">
    </form>
    <a href="{% url 'list' %}">
        <button>No</button>
    </a>
{% endblock container %}
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi ogrenciapp/templates/ogrenciapp/ogrenci_detay.html bölgesi

{% extends 'fscohort/base.html' %}

{% block container %}
    {{student.number}} - {{student.first_name}} {{student.last_name}}
    <br>
    <a href="{% url 'update' student.id %}"><button>Update</button></a>
    <a href="{% url 'delete' student.id %}"><button>Delete</button></a>
{% endblock container %}
####################################################################################################
#
#
#
#
#
####################################################################################################
from django.apps import AppConfig

class OgrenciConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ogrenciapp'
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi ögrenciapp/models.py bölgesi

from django.db import models

class ÖgrenciModeli(models.Model):
    isim = models.CharField(max_length=30)
    numara = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.isim}"
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi ögrenciapp/admin.py bölgesi

from .models import ÖgrenciModeli

admin.site.register(ÖgrenciModeli)
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi ögrenciapp/forms.py bölgesi

from django import forms
from .models import OgrenciModeli

class StudentForm(forms.ModelForm):
    # models'deki Ögrenci modeline git, oradaki isim ve numarayi al.
    class Meta:
        model = OgrenciModeli
        fields = ["isim", "numara"]
        labels = {"isim": "Ögrenci Adi Soyadi", "numara": "Ögrenci Numarasi"}
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi ögrenciapp/views.py bölgesi

from django.shortcuts import render,redirect
from .models import Ogrenci
from .forms import OgrenciFormu

def index(request):
    return render(request,'ogrenciapp/index.html')

def ogrenci_listesi(request):
    students=Ogrenci.objects.all()
    bunlariGönder = {
        'students':students
    }
    return render(request, 'ogrenciapp/ogrenci_listesi.html', bunlariGönder)

def ogrenci_ekle(request):
    form=OgrenciFormu()
    if request.method=='POST':
        form=OgrenciFormu(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("list")
    bunlariGönder = {
      'form':form  
    }
    return render(request,'ogrenciapp/ogrenci_ekle.html', bunlariGönder)

def ogrenci_guncelle(request,id ):
    student=Ogrenci.objects.get(id=id)
    form=OgrenciFormu(instance=student)
    if request.method=='POST':
        form=OgrenciFormu(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    bunlariGönder = {
        'form':form
    }
    return render(request,'ogrenciapp/ogrenci_guncelle.html', bunlariGönder)

def ogrenci_sil(request,id):
    student=Ogrenci.objects.get(id=id)
    if request.method=='POST':
        student.delete()
        return redirect("list")
        
    bunlariGönder = {
            'student':student
    }
    return render(request,"ogrenciapp/ogrenci_sil.html", bunlariGönder)
    
def ogrenci_detay(request, id):        
    student = Ogrenci.objects.get(id=id)
    bunlariGönder = {
        'student': student
    }
    return render(request, 'ogrenciapp/ogrenci_detay.html', bunlariGönder)
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi ogrenciapp/urls.py bölgesi

from django.urls import path
from .views import index, ogrenci_listesi, ogrenci_ekle, ogrenci_guncelle, ogrenci_sil, ogrenci_detay

urlpatterns = [
    path("", index, name="index"),
    path('liste/', ogrenci_listesi , name='liste'),
    path('ekle/', ogrenci_ekle, name='ekle'),
    path('guncelle/<int:id>', ogrenci_guncelle, name='guncelle'),
    path('sil/<int:id>', ogrenci_sil, name='sil'),
    path('ogrenci/<int:id>', ogrenci_detay, name="detay"),

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('ogrenciapp.urls')),
]
####################################################################################################
