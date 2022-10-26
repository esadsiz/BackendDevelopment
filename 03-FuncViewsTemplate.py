####################################################################################################
# Burasi index.html bölgesi

# Önce bulundugumuz app klasörünün icinde templates adinda bir klasör olustururuz.
# Daha sonra bu templates klasörünün altinda, bulundugumuz app klasörüyle ayni isimde bir baska klasör olustururuz.
# Bunun sebebi Django'da bir kafa karisikligina sebep olmamak.
# Onun altinda da bir index.html dosyasi acariz.

{%load static%} # index.css'i, html dosyamiza böyle baglariz.
<head>
  <link rel="stylesheet" href="{ % static 'appenes/index.css' %}" />
</head>

<h1>Bu sayfa öylesine bir sayfa</h1>
{{request.user}}
{{baslik}} # ornek icindeki baslik degerine bu sekilde ulasabildik. <br />
{{baslik | title}} # title, string degerin bas harfini büyük yapar. ne tür filtreler var arastirip bakabilirsin.
{% for eleman in listem %} {% if eleman == 3 %} {{eleman}} {%endif%} {%endfor%} # DTL'de bir for ve if döngüsü uyguladik.
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi index.css bölgesi

# Önce bulundugumuz app klasörünün icinde static adinda bir klasör olustururuz.
# Daha sonra bu static klasörünün altinda, bulundugumuz app klasörüyle ayni isimde bir baska klasör olustururuz.
# Bunun sebebi Django'da bir kafa karisikligina sebep olmamak.
# Onun altinda da bir index.css dosyasi acariz.

body {
  background-color: beige;
}
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi views.py bölgesi

from django.shortcuts import render

def templateGetir(request):
    print("bu kisim, bu fonksiyon cagrildiginda terminale basilir.")
    print(request)
    print(request.method)
    print(request.COOKIES)
    print(request.path)
    print(request.user)
    print(request.META)
    bunlariGonder = {
        'baslik' : 'djangosuper',
        'listem' : [1,3,5]
    }
    return render(request, 'appenes/index.html', bunlariGonder) # index.html dosyasini ilgili sayfaya basar.
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi urls.py bölgesi

from django.urls import path
from .views import templateGetir

urlpatterns = [
    path('templateSayfasi', templateGetir),
]
####################################################################################################
