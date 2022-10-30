# Konsol üzerinden user yaratma.
# Öncelikle terminale python manage.py shell yazariz. Terminalimiz artik bir python bölgesi.
# Daha sonra from django.contrib.auth.models import User yazariz.
# kullanici1 = User.objects.create_user("esadsiz", email="enes@enes.com yazar enter'a tiklariz.
# kullanici1.first_name = "Enes" yazar Enter'a tiklariz.
# kullanici1.set_password(sifresifre)
# kullanici1.save() yazar, tekrar Enter'a tiklariz.
# Kullanicilarimiz artik admin panel'deki Users kisminda.

####################################################################################################
TAMAM
# Burasi main/urls.py bölgesi

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_example.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # authentication icin bu satiri ekleriz.
]
####################################################################################################
#
#
#
#
####################################################################################################
TAMAM
# Burasi kullaniciapp/urls.py bölgesi

from django.urls import path, include
from .views import (home, special, register)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name="indexPathi"),
    path('special/', special, name="special"),
    path('register/', register, name="register"),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name="registration/password_change.html"), name="password_change")
    # django'nun bize hazir olarak sundugu template yerine kendi templateimizi kullanmak istersek böyle yapariz.
]
####################################################################################################
#
#
#
#
#
#
####################################################################################################
TAMAM
# Burasi kullaniciapp/templates/kullaniciapp/index.html bölgesi

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    # user authenticated ise; user burada default bir terim.
    {% if user.is_authenticated %}
        <h1>
            # database'den username'imizi ceker.
            Hello {{user.username | title}}    
        </h1>    
        {% comment %}
        <a href="{% url 'logout' %}">Logout</a>
        {% endcomment %}
            
    # user authenticated degil ise;    
    {% else %}
        <h1>Hello, please login to see the page.</h1>
        {% comment %}
        <a href="{% url 'login %}">Login</a> 
        {% endcomment %}
    {% endif %}
</body>
</html>
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullaniciapp/templates/registration/register.html bölgesi

<h1>Register Page</h1>

<form action="" method="post">
    {% csrf_token %}
    {{ form.as_p }} # django bize register icin form düzenini hazir olarak sunar.
    <input type="submit" value="Register">
</form>
####################################################################################################
#
#
#
#
####################################################################################################
TAMAM
# Burasi kullaniciapp/templates/registration/login.html bölgesi

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="" method="post">
        {% csrf_token %}
        {{ form.as_p }} # burada cagiracagimiz formu herhangi bir view icerisinde yazmamiza gerek yok. django bunu bizim icin zaten olusturmustur.
        <input type="submit" value="Login">
    </form>
</body>
</html>
####################################################################################################
#
#
#
#
####################################################################################################
TAMAM
# Burasi main/settings.py bölgesi

LOGIN_REDIRECT_URL = "homePathi" # kullanici login oldugunda homePathi'ne yönlendirir.

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # sifre resetleme isleminde mailimize gönderilen mailin aynisini konsola bastirir.

# Ayrica kullaniciapp isimli appimizi INSTALLED_APPS icinde en üst siraya koymaliyiz ki,
# django render asamasinda kendi default html sayfalari yerine bizimkini render etsin. 
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullaniciapp/templates/registration/password_change.html bölgesi

<h1>Password Change</h1>

<form action="" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Update">
</form>
####################################################################################################
#
#
#
#
#####################################################################################################
# Burasi kullaniciapp/templates/registration/password_change_done.html bölgesi

<h1>Password change successful</h1>
<p>Your password was changed.</p>
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi kullaniciapp/templates/registration/password_reset.html bölgesi

<h1>Password Reset</h1>

<form action="" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Reset">
</form>
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullaniciapp/templates/registration/password_reset_done.html bölgesi

<p>We’ve emailed you instructions for setting your password, if an account exists with the email you entered. You
    should receive them shortly.</p>

<p>If you don’t receive an email, please make sure you’ve entered the address you registered with, and check your
    spam folder.</p>
#####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullaniciapp/templates/registration/password_reset_confirm.html bölgesi

<h1>Password Reset Confirm</h1>

<form action="" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Reset">
</form>
####################################################################################################
#
#
#
#
####################################################################################################
# Burasi kullaniciapp/templates/registration/password_reset_complete.html bölgesi

<h1>Password reset complete</h1> 
<p>Your password has been set. You may go ahead and log in now.</p>
<a href="{% url 'login' %}">Login</a>
#####################################################################################################
#
#
#
#
#
####################################################################################################
TAMAM
# Burasi kullaniciapp/templates/kullaniciapp/special.html bölgesi

<h1>This is a special page!</h1>
<h3>Hello {{ request.user }}! You are lucky to see this page!</h3>
####################################################################################################
#
#
#
#
#
####################################################################################################
TAMAM
# Burasi kullaniciapp/views.py bölgesi

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'kullaniciapp/index.html')

@login_required
def special(request):
    return render(request, "kullaniciapp/special.html")

# kullanici kaydi icin view. django, login'in aksine register icin view'i bizim olusturmamizi ister. 
def register(request):
    form = UserCreationForm(request.POST or None)
    # UserCreationForm django'nun kendi sundugu form düzenini cagirir.
    # request.POST'un icerisinde bir sey varsa parantez icine onu koy, yoksa hicbir sey koyma, sadece render et.
    # Daha önce yaptigimiz if request.method == 'POST': ... isleminin kisaltilmis hali.
    if form.is_valid():
        form.save()
        # username = form.cleaned_data.get("username")
        # password = form.cleaned_data.get("password2") # parantez icleri html taglarindaki name isimleridir.
        # user = authenticate(username=username, password=password)
        # login(request, user)
        # return redirect("home")
        # kullanici register oldugunda otomatik giris yapsin istiyorsak, bu satirlari ekleriz.
        return redirect("login")
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)
####################################################################################################
