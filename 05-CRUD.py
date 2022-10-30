####################################################################################################
# Burasi ogrenciapp/templates/ogrenciapp/base.html bölgesi

<!DOCTYPE html>
{% load static %}

<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href=" {% static 'ogrenciapp/style.css' %}  " />
    <title>Document</title>
  </head>
  <body>
    <h1> Merhaba esadsiz </h1>
    {% comment %} {% include "users/navbar.html" %} {% endcomment %}
    <div style="margin-top: 100px; margin-bottom: 100px" class="container">
      {% block container %}{% endblock container %}
    </div>
    <script src="{% static 'ogrenciapp/zamanlayici.js' %}"></script>
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

{% extends "ogrenciapp/base.html" %}

{% block container %}

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

{% extends "ogrenciapp/base.html" %}

{% block container %}
    <ul>
        {% for eleman in ogrencileriBastir %}
        <a href="{% url 'detail' eleman.id %}">
        <li>{{ eleman.numara}} - {{eleman.isim}}</li>
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

{% extends 'ogrenciapp/base.html' %}

{% block container %}
    <h2>Ögrenci Ekle</h2>
    <form action="" method="POST">
        {% csrf_token %}                   
        {{formuBastir.as_p}}						   
        <input type="submit" value="Ekle">
    </form>
{% endblock container %}
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi ögrenciapp/templates/ögrenciapp/ogrenci_guncelle.html bölgesi

{% extends 'ogrenciapp/base.html' %}

{% block container %}
    <h2>Ögrenci Güncelle</h2>
    <form action="" method="POST">
        {% csrf_token %}                   
        {{formuBastir.as_p}}						   
        <input type="submit" value="Güncelle">
    </form>
{% endblock container %}
####################################################################################################
#
#
#
#
#####################################################################################################
# Burasi ögrenciapp/templates/ögrenciapp/ogrenci_sil.html bölgesi

{% extends 'ogrenciapp/base.html' %}

{% block container %}
    <form action="" method="POST">
        <p> Emin misiniz? {{ ogrenciyiBastir }}</p>
        {% csrf_token %}
        <input type="submit" value="Evet">
    </form>
    <a href="{% url 'listePathi' %}">
    # butona basildiginda bizi listePath'ine yönlendirir.
        <button>Hayir</button>
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

{% extends 'ogrenciapp/base.html' %}

{% block container %}
    {{ogrenciyiBastir.numara}} - {{ogrenciyiBastir.isim}}
    <br>
    <a href="{% url 'guncellePathi' ogrenciyiBastir.detayId %}"><button>Güncelle</button></a>
    <a href="{% url 'silPathi' ogrenciyiBastir.detayId %}"><button>Sil</button></a>
    # Güncelle butonu guncellePathi'ne, Sil butonu silPathi'ne yönlendirir.
{% endblock container %}
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi ögrenciapp/models.py bölgesi

from django.db import models

class OgrenciModeli(models.Model):
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

from .models import OgrenciModeli

admin.site.register(OgrenciModeli)
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
# Burasi ogrenciapp/views.py bölgesi

from django.shortcuts import render,redirect
from .models import Ogrenci
from .forms import OgrenciFormu

def index(request):
    return render(request,'ogrenciapp/index.html')

def ogrenci_listesi(request):
    butunOgrenciler=Ogrenci.objects.all()
    # .object.all() Ogrenci modeli ile olusturulmus bütün objeleri ceker.
    bunlariGonder = {
        'ogrencileriBastir': butunOgrenciler
    }
    return render(request, 'ogrenciapp/ogrenci_listesi.html', bunlariGonder)

def ogrenci_ekle(request):
    formuAl=OgrenciFormu()
    if request.method=='POST':
        formuAl=OgrenciFormu(request.POST)
        print(formuAl)
        if formuAl.is_valid():
            formuAl.save()
            return redirect("listePathi")
    bunlariGonder = {
      'formuBastir':formuAl  
    }
    return render(request,'ogrenciapp/ogrenci_ekle.html', bunlariGonder)

def ogrenci_guncelle(request, guncellecekId):
    # guncellenecek objeyi, yani kisiyi cek. (id'sine göre)
    ogrenciyiAl=Ogrenci.objects.get(id=guncellecekId)
    # simdi cektigimiz objeyi forma birakalim.
    formuAl=OgrenciFormu(instance=ogrenciyiAl)
    if request.method=='POST':
        formuAl=OgrenciFormu(request.POST, instance=ogrenciyiAl)
        if formuAl.is_valid():
            formuAl.save()
            return redirect('listePathi')
    bunlariGonder = {
        'formuBastir':formuAl
    }
    return render(request,'ogrenciapp/ogrenci_guncelle.html', bunlariGonder)

def ogrenci_sil(request,silinecekId):
    # silinecek objeyi, yani kisiyi cek. (id'sine göre)
    ogrenciyiAl=Ogrenci.objects.get(id=silinecekId)
    if request.method=='POST':
        ogrenciyiAl.delete()
        return redirect("listePathi")
    bunlariGonder = {
        'ogrenciyiBastir':ogrenciyiAl
    }
    return render(request,"ogrenciapp/ogrenci_sil.html", bunlariGonder)
    
def ogrenci_detay(request, detayId):        
    ogrenciyiAl = Ogrenci.objects.get(id=detayId)
    bunlariGonder = {
        'ogrenciyiBastir': ogrenciyiAl
    }
    return render(request, 'ogrenciapp/ogrenci_detay.html', bunlariGonder)
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
    path('liste/', ogrenci_listesi , name='listePathi'),
    path('ekle/', ogrenci_ekle, name='eklePathi'),
    path('guncelle/<int:guncellenecekId>', ogrenci_guncelle, name='guncellePathi'),
    path('sil/<int:silinecekId>', ogrenci_sil, name='silPathi'),
    path('ogrenci/<int:detayId>', ogrenci_detay, name="detayPathi"),

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
#
#
#
#
#
####################################################################################################
# Burasi ogrenciapp/static/ogrenciapp/style.css bölgesi

h1 {
  background-color: rgb(128, 27, 116);
}
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi ogrenciapp/static/ogrenciapp/zamanlayici.js bölgesi

let element = document.querySelector('.alert');

setTimeout(function () {
  element.style.display = 'none';
}, 3000);
####################################################################################################
