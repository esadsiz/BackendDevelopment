# Öncelikle terminale pip install python-decouple yazarak modülümüzü yükleriz.
# Daha sonra settings.py dosyasina su satiri ekleriz: from decouple import config
# Sonra ise genel proje klasörümüzün icinde .env isminda dosya olustururuz.
# settings.py'daki SECRET_KEY'imizi alir, tirnaksiz bir sekilde .env dosyasina kopyalariz.
# Sonra da settings.py'daki SECRET_KEY'imizi asagidaki gibi degistiririz ve eklemelerde bulunuruz.

####################################################################################################
# Burasi .env bölgesi

SECRET_KEY=django-insecure-og7whxi)t2!9a$ksvpy&qylwh*=cjq=5ard_17!1)zpglzsrkb
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi settings.py bölgesi

SECRET_KEY=config("SECRET_KEY") # bu, .env'de SECRET_KEY'i bul, bana getir demek
MEDIA_ROOT = BASE_DIR / 'media/'
MEDIA_URL = '/media/'
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi models.py bölgesi

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi admin.py bölgesi

from .models import Student

admin.site.register(Student)
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi studentapp/templates/studentapp/base.html bölgesi

<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- <link rel="stylesheet" href="../static/css/style.css" /> -->
    <link rel="stylesheet" href="{% static 'student/css/style.css' %}" />
  </head>
  <body>
    {% block container %}{% endblock container %}
  </body>
</html>
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi studentapp/templates/studentapp/index.html bölgesi

{% extends "student/base.html" %} {% block container %}
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
# Burasi views.py bölgesi

from django.shortcuts import render

def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    return render(request,'student/student.html')
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi ana urls.py bölgesi

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from student.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('student/', include('student.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# sonuna burasi eklenir. bu bir önceki derste gördügümüz static dosyalari acilabilir yapma islemi.
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi student/urls.py bölgesi

from django.urls import path

from .views import student_page

urlpatterns = [
    path('', student_page, name='student'),
]
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi student/forms.py bölgesi

from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    number = forms.IntegerField(required=False)
    profile_image = forms.ImageField(required=False)
####################################################################################################
