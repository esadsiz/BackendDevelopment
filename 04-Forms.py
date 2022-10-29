# Öncelikle terminale pip install python-decouple yazarak modülümüzü yükleriz.
# Daha sonra settings.py dosyasina su satiri ekleriz: from decouple import config
# Sonra ise genel proje klasörümüzün icinde .env isminda dosya olustururuz.
# settings.py'daki SECRET_KEY'imizi alir, tirnaksiz bir sekilde .env dosyasina kopyalariz.
# Sonra da settings.py'daki SECRET_KEY'imizi asagidaki gibi degistiririz ve eklemelerde bulunuruz.

####################################################################################################
# Burasi main/.env bölgesi

SECRET_KEY=django-insecure-og7whxi)t2!9a$ksvpy&qylwh*=cjq=5ard_17!1)zpglzsrkb
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi main/settings.py bölgesi

SECRET_KEY=config("SECRET_KEY") # bu, .env'de SECRET_KEY'i bul, bana getir demek
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi ögrenciapp/templates/ögrenciapp/base.html bölgesi

# Burada genelde bizim navbarlarimiz footerlarimiz bulunur.
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'ögrenciapp/css/style.css' %}" />
  </head>
  <body>
    {% block container %}
    {% endblock container %}
  </body>
</html>
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi ögrenciapp/templates/ögrenciapp/index.html bölgesi

# base.html'deki bütün yapiyi al, ve block container'larin arasina sunlari ekle.
{% extends "ögrenciapp/base.html" %}

{% block container %}

<h1>Home Page</h1>
<h3>Student App</h3>

{% endblock container %}
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi ögrenciapp/templates/ögrenciapp/ögrenci.html bölgesi

# base.html'deki bütün yapiyi al, ve block container'larin arasina sunlari ekle.
{% extends "ögrenci/base.html" %} 

{% block container %}

<form action="" method="post">
    {% csrf_token %} {{ form.as_p }}
    # csrf_token, hackerlara karsi bir önlem alir.
    # form.as_p, form bilesenlerini alt alta siralamaya yarar.
    <input type="submit" value="GÖNDER" />
 </form>

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
#
####################################################################################################
# Burasi ögrenciapp/forms.py bölgesi

from django import forms
from .models import ÖgrenciModeli

class ÖgrenciFormu(forms.ModelForm):
    # models'deki Ögrenci modeline git, oradaki isim ve numarayi al.
    class Meta:
        model = ÖgrenciModeli
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

from django.shortcuts import render, redirect
from .forms import ÖgrenciFormu

def index(request):
    return render(request, 'ögrenciapp/index.html')

def ögrenci_sayfasi(request):
    form = ÖgrenciFormu()
    if request.method == "POST":
        form = ÖgrenciFormu(request.POST, request.FILES)
        if form.is_valid():
            form.save() # verileri otomatik olarak veri tabanina kaydeder.
            return redirect("indexPathi")
    context = {
        'form': form
    }
    return render(request, 'ögrenci/ögrenci.html', context)
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi ögrenciapp/urls.py bölgesi

from django.urls import path
from .views import ögrenci_sayfasi

urlpatterns = [
    path('', ögrenci_sayfasi, name='ögrenciPathi'),
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
from ögrenciapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='indexPathi'),
    path('ögrenci/', include('ögrenciapp.urls')),
]
####################################################################################################
