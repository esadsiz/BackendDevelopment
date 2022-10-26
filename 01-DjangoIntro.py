# Terminalde python version kontrol yapma:
# python --version

# Terminalde sanal ortam olusturma
# python -m venv ortamismi

# Olusturulan sanal ortami aktif hale getirme
# (source) .\ortamismi\Scripts\activate

# Olusturulan sanal ortami deaktif hale getirme
# deactivate

# Olusturulan sanal ortamda ne var ne yok görme (python kurulu mu görmek icin kullanilabilir)
# pip freeze

# django'yu kurma
# pip install django

# django'da proje olusturma
# django-admin startproject projeismi
# django-admin startproject projeismi . (eger ic ice cift klasör olusturmasini istemiyorsak)

# olusturulan projeyi calistirma
# python manage.py runserver

# proje icinde app olusturma
# python manage.py startapp appismi

# sonradan olusturulan her app'in, settings.py icindeki INSTALLED_APPS=[]'e "appismi" seklinde eklenmesi gerekir.

####################################################################################################
# Burasi views.py bölgesi

# view'lerimizi burada olusturuyoruz.

# Bir http istegi gerceklestirecegimiz icin;
from django.http import HttpResponse

def anasayfa(istek):
    return HttpResponse("<h1>Merhaba Enes</h1>")
# Bu viewi urls.py icinde ilgili yere göndermeliyiz.
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi settings.py bölgesi
# Olusturulan app'i INSTALLED_APPS'e girmemiz lazim.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'appismi' # olusturulan app klasörünün ismi
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
from projeklasörü.appismi.views import anasayfa

urlpatterns = [
    path("", anasayfa) #tirnak ici bossa anasayfa'ya yönlendir.
    path("ilksayfa", adminpaneli ) #.../ilksayfa pathine girdigimizde adminpaneli view'ini görürürüz.
    path("yönlendirme",include(appismi.urls)) # girilen path .../yönlendirme ise ilkapp klasöründeki urls'e git (appler urls dosyasi icermez, kendimiz olustururuz.)
]
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi appismi klasörü icindeki urls.py bölgesi

from django.urls import path, include
from projeklasörü.appismi.views import anasayfa

urlpatterns = [
        path("", yönlendirilmisview) # girilen path .../yönlendirme ise yönlendirilmisview viewini görürüz.
        path("/icicesayfa", icicesayfaview) # girilen path .../yönlendirme/icicesayfa ise icicesayfaview viewini görürüz.
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
