# UFAK BIR NOT #
# Repo'dan cekilmis bir projenin environmentini yüklemek icin;
pip install -r requirements.txt

####################################################################################################
# Burasi models.py bölgesi

from tabnanny import verbose
from django.db import models

# Databaseimizde bir Ögrenci tablosu olusturalim.

class Ögrenci(models.Model):
    ULKELER = [
    ("TR", "Türkiye"),
    ("DE", "Almanya")
    ]

    isim = models.CharField("Adi", max_length=30) # isim isimli sütunum karakter alsin, ve maksimum 30 karakter olsun.
    numara = models.IntegerField("Numarasi") # numara isimli sütunum rakam, numara, sayi alsin.
    ülke = models.CharField(max_length=2, choices=ULKELER, default="TR") # ögrencinin ülkesini ULKELER verisinden sectir.
    aciklama = models.TextField(null=True, blank=True) # aciklama isimli sütunum uzun bir text alani alsin. null=True ya da blank=True bos birakilabilir demek.
    kayittarihi = models.DateField("Kayit Tarihi", auto_now_add=True) # kayittarihi isimli sütun otomatik tarih atar. Tablo üzerinde sütun basligi "Kayit Tarihi seklinde görünür."
    songiriszamaani = models.DateTimeField(auto_now=True) # DateTimeField hem zamani hem tarihi atar. auto_now ile auto_now_add arasindaki fark, auto_now'in otomatik degisebilir olmasi.
    aktifmi = models.BooleanField(default=True) # BooleanField true ya da false alir.
    profilresmi = models.ImageField(upload_to="media/") # upload edilen resim media klasörüne yüklensin.
    # resim islemlerini kontrol edebilecegimiz metodu yüklemek icin terminale pip install pillow yazariz.
    # daha sonra settings.py'a gider, MEDIA_URL="media/" satiri ekleyerek bu media klasörünü tanitiriz.
    # artik admin paneli üzerinden bir resim yükledigimizde, proje dosyasi icinde otomatik olarak media klasörü olusur ve resim bu klasörün icine kaydedilir.

    def __str__(self):
        return (f"{self.numara} - {self.isim}")
    # admin paneli icerisinde olusturulacak her bir obje Ögrenci object(1) vs yerine yazili sekilde görünür.

    class Meta:
        ordering = ['numara']
    # olusturulmus objelerin admin paneli icindeki gösterimi numara sirasina göre olsun.
        verbose_name_plural = "Ögrenci Listesi"
    # admin panelde görünen tablo ismini Ögrenci_listesi seklinde günceller.
 
    # olusturdugumuz bu tablodan pythonun haberi olmasi icin terminale sunu yazariz. yeni bir veri girisi yaptiktan sonra degisiklikleri yakalamak icin de kullanilir.
    # python manage.py makemigrations
    
    # bu komutla da django database'e gidip bu tabloyu olusturur. yeni bir veri girisi yaptiktan sonra veritabanini güncellemek icin de kullanilir.
    # python manage.py migrate

    # simdi bir admin paneli ayaga kaldiralim.
    # python manage.py createsuperuser
    # daha sonra email vs gibi bizden istenen bilgileri gireriz.

    # daha sonra python manage.py runserver yazarak serveri calistiralim.
    # /admin pathine gidelim. karsimiza bir admin paneli cikacak.
    # bu /admin pathi, urls.py icinde otomatik tanimlidir.

# olusturdugumuz tabloyu admin paneli icerisine yüklemek icin admin.py icinde cagiririz.
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi admin.py bölgesi

from .models import Ögrenci

admin.site.register(Ögrenci)
####################################################################################################
#
#
#
#
#
####################################################################################################
# Burasi urls.py bölgesi

# media/ ile ilgili gelen istekleri, MEDIA_URL'deki klasörden cagir.

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# burada path kullanilmaz, path dinamik adreslerde kullanilir, resim, js, video gibi seyler statiktir.
####################################################################################################
#
#
#
#
#
#
#
#
#
#
####################################################################################################
# Burasi relations app'ine ait models.py bölgesi

from django.db import models

class Yazar(models.Model):
    yazarismi = models.CharField(max_length=30)

class Kitap(models.Model):
    kitapismi = models.CharField(max_length=30)
    kitabinyazari=models.OneToOneField(Yazar, on_delete=models.CASCADE) # yazar ile kitabinyazari sütunu üzerinde one to one bir iliski kur.
    # kitabinyazari özelliklerini Yazar'dan alir. 
    # on_delete=models.CASCADE ise Yazar tablosundaki herhangi bir yazar silindiginde ona ait kitabi da otomatik sil demek. on_delete metodlarina kendin bakabilirsin.

# Admin paneline gidilir. Önce öregin 3 adet Yazar olusturulur.
# Daha sonra Kitap olusturulmak istendiginde, altta bize bir secenek sunuldugunu görürüz, Yazari kim? secenegi.
# Kurulu iliski one to one oldugu icin bir kitaba bir yazar bir kez atanabilir.
####################################################################################################
#
#
#
#
#
#
#
#
#
#
####################################################################################################
# Burasi relations app'ine ait models.py bölgesi

from django.db import models

class Kitap(models.Model):
    kitapismi = models.CharField(max_length=30)


class Yazar(models.Model):
    yazarismi = models.CharField(max_length=30) 
    yazdigikitaplar=models.ForeignKey(Kitap, on_delete=models.CASCADE) # yazar ile yazdigikitaplar sütunu üzerinde one to many bir iliski kur.
    # yazdigikitaplar özelliklerini Kitap'tan alir.
    # on_delete=models.CASCADE ise Kitap tablosundaki herhangi bir kitap silindiginde ona ait yazari da otomatik sil demek. on_delete metodlarina kendin bakabilirsin.

# Admin paneline gidilir. Önce örnegin 3 adet Kitap olusturulur.
# Daha sonra Yazar olusturulmak istendiginde, altta bize secenekler sunuldugunu görürüz, Yazdigi kitaplar? secenekleri.
# Kurulu iliski one to many oldugu icin bir yazara birden fazla kitap atanabilir.  
####################################################################################################
#
#
#
#
#
#
#
#
#
#
####################################################################################################
# Burasi relations app'ine ait models.py bölgesi

from django.db import models

class Kitap(models.Model):
    kitapismi = models.CharField(max_length=30)


class Okuyucu(models.Model):
    okucuyuismi = models.CharField(max_length=30) 
    okudugukitaplar=models.ManyToManyField(Kitap) # okuyucu ile yazdigikitaplar sütunu üzerinde many to many bir iliski kur.
    # many to many'de on_delete kullanilmaz.
    # okudugukitaplar özelliklerini Kitap'tan alir.
    # burada mantik sudur: bir kitabi birden fazla kisi okumus olabilir, bir kisi de birden fazla kitap okumus olabilir.

# Admin paneline gidilir. Önce öregin 3 adet Kitap olusturulur.
# Daha sonra Okuyucu olusturulmak istendiginde, altta bize secenekler sunuldugunu görürüz, Okudugu kitaplar? secenekleri.
# Kurulu iliski many to many oldugu icin bir okuyucuya birden fazla kitap atanabilir, ayni sekilde bir kitap da birden fazla okuyucuya atanabilir.
####################################################################################################

# UFAK BIR NOT #
# PostgreSQL'i Django'ya baglamak icin;
# pgAdmin üzerinden bir database olusturulur. adi djangodb olsun.
# daha sonra projenin settings.py ayarlarinda; DATABASES = {} kismi yoruma alinir, yani iptal edilir.
# yerine;
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangodb',
        'USER': 'dbuser',
        'PASSWORD' : 'dbpass',
        'HOST': 'localhost',
        'PORT' '5432'
    }
} # eklenir.
# terminale pip install psycopg2 ya da pip install psycopg2-binary yazilarak ilgili modüller yüklenir.
# python manage.py makemigrations ve python manage.py migrate ile de, tablolarimizin PostgreSQL arayüzünde, ilgili veritabaninin Tables kismina yüklendigini görürüz.
# sistemimiz artik PostgreSQL'e bagli.
