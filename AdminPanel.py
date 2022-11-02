################################################################################################
# pip install Faker: veri tabanimiza fake veriler girer. Test amacli kullanilir.
# Daha sonra python manage.py shell yazarak shell'e gireriz. Ardindan su komutlari gireriz:

# from urunapp.models import UrunModeli
# from faker import Faker
# faker = Faker()
# for i in range(1,200):
# urun = UrunModeli(urunismi=faker.name(), urunaciklamasi=faker.paragraph(), stok_durumu=False)
# urun.save()

#####

# pip install django-ckeditor word tarzi bir text editör paketidir.
################################################################################################
#
#
#
#
#
################################################################################################

from django.db import models
from ckeditor.fields import RichTextField

class UrunModeli(models.Model):
    urunismi = models.CharField(max_length=100)
    urunaciklamasi = models.TextField(blank=True, null=True)
    # urunaciklamasi = RichTextField()
    tarih_olustur = models.DateTimeField(auto_now_add=True)
    tarih_guncelle = models.DateTimeField(auto_now=True)
    stok_durumu = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
    
    def __str__(self):
        return self.urunismi

    def inceleme_sayisi(self):
        count = self.inceleme_sayisi()
        return count

####################################################################################################

class Inceleme(models.Model):
    product = models.ForeignKey(UrunModeli, on_delete=models.CASCADE, related_name='incelemeler')
    # Iki tablo arasinda iliski kurmak icin ForeignKey kullanilmistir.
    inceleme = models.TextField()
    is_released = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Inceleme'
        verbose_name_plural = 'Incelemeler'
        
        
        
 ###########################################################

from django.contrib import admin
from .models import UrunModeli, Inceleme, IncelemeInline
from django.utils import timezone

admin.site.site_title = "Site Basligi"
admin.site.site_header = "Sitenin Admin Paneli"  
admin.site.index_title = "Sitenin Admin Portalina Hosgeldiniz"

class UrunModeliAdmin(admin.ModelAdmin):
    list_display = ("urunismi", "tarih_olustur", "stok_durumu", "tarih_guncelle", "x_gun_once_eklendi")
    # Hangi propertyleri istersek, onlari liste sayfasinda görebiliriz.
    list_editable = ( "stok_durumu", )
    # Bu property liste üzerinden edit edilebilir.
    list_display_links = ("tarih_olustur","urunismi" )
    # Bu property tiklanabilir olur.
    list_filter = ("stok_durumu", "tarih_olustur")
    # Sagda bir filtre paneli cikar. Listeyi belirttigimiz propertylere göre filtreleyebiliriz.
    ordering = ("urunismi",)
    # Listeyi property'e göre siralayabiliriz.
    search_fields = ("urunismi",)
    # Belirttigimiz property icin bir elemani liste icinde arayabiliriz.
    prepopulated_fields = {'slug' : ('urunismi',)}
    # url'de urunismi acikca görünmez, onun yerine unique bir ifade görünür.
    list_per_page = 25
    # sayfa basina kac liste elemani görüntüleneceginizi seceriz.
    date_hierarchy = "tarih_guncelle"
    # üstte takvim mantiginda bir tarih paneli olusturur. istenilen aya ya da yila gidilebilir.
    fields = (('urunismi', 'slug'), 'urunaciklamasi', "stok_durumu")
    # elemanlarin Change bölümünde hangi sirada hizada görüneceklerini seceriz.
    # fieldset kullandığımız zaman bunu kullanamayız. fieldset daha fazla fonksiyona sahip. arastir, bak.

    inlines = (IncelemeInline)

    actions = ("stok_sifirla",)
    def stok_sifirla(self, request, queryset):
        count = queryset.update(stok_durumu=False)
        self.message_user(request, f"{count} ürünün stok degeri sifirlandi.")
    stok_sifirla.short_description = 'Ürünleri stoktan cikar'
    
    def x_gun_once_eklendi(self, isimÖnemsiz):
        fark = timezone.now() - isimÖnemsiz.tarih_olustur
        return fark.days

admin.site.register(UrunModeli, UrunModeliAdmin)

####################################################################################################

class IncelemeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',)

admin.site.register(Inceleme, IncelemeAdmin)

####################################################################################################

class IncelemeInline(admin.TabularInline):  # StackedInline farklı bir görünüm aynı iş
    '''Tabular Inline View for '''
    model = Inceleme
    extra = 1
    classes = ('collapse',)
    # min_num = 3
    # max_num = 20

admin.site.register(IncelemeInline)



