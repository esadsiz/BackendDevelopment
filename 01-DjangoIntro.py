# Terminalde python version kontrol yapma:
# python --version

# Terminalde sanal ortam olusturma
# python -m venv ortamismi

# Olusturulan sanal ortami aktif hale getirme
# source ./ortamismi/Scripts/activate

# Olusturulan sanal ortami deaktif hale getirme
# deactivate

# Olusturulan sanal ortamda ne var ne yok görme (python kurulu mu görmek icin kullanilabilir)
# pip freeze

# django'yu kurma
# pip install django

# django'da proje olusturma
# django-admin startproject projeismi

# sonradan olusturulan her app'in settings.py icindeki INSTALLED_APPS=[]'e "appismi" seklinde eklenmesi gerekir.

# olusturulan projeyi calistirma
# python manage.py runserver

# proje icinde app olusturma
# python manage.py startapp ilkapplication

####################################################################################################
# Burasi views.py bölgesi

# view'lerimizi burada olusturuyoruz.

# Bir http istegi gerceklestirecegimiz icin;
from django.http import HttpResponse
def anasayfa(istek):
    return HttpResponse("Merhaba Enes")

# Bu viewi urls.py icinde ilgili yere göndermeliyiz.
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi settings.py bölgesi
# Olusturulan app'i ISNTALLED_APPS'e girmemiz lazim.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'ilkapp' # olusturulan app klasörünün ismi
]

####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi urls.py bölgesi

from django.urls import path
from firstdjango.ilkapplication1.views import anasayfa

urlpatterns = [
    path("", anasayfa) #tirnak ici bossa anasayfa'ya yönlendir.
    path("ilksayfa", adminpaneli ) #.../ilksayfa pathine girdigimizde adminpaneli view'ini görürürüz.
    path("yönlendirme",include(ilkapp.urls)) # girilen path .../yönlendirme ise ilkapp klasöründeki urls'e git (appler urls icermez, bunu kendimiz olustururuz.)
]
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi ilkapp klasörü icindeki urls.py bölgesi

from django.urls import path, include
from firstdjango.ilkapplication1.views import anasayfa

urlpatterns = [
        path("yönlendirme", yönlendirilmisview) # girilen path .../yönlendirme ise yönlendirilmisview viewini görürüz.
        # tirnak icinde artik yönlendirme yazmasi sart da degil. yine de .../yönlendirme pathi icinde yönlendirilmisview pathini görürüz.

]
####################################################################################################
#
#
#
#
#
####################################################################################################

# terminalde pip freeze > requierements.txt yazarsak, projedeki yüklü seylerin bilgisini requirements.txt isminde bir dosya olusturarak onun icine atar.

####################################################################################################


