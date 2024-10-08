from django.urls import path

from . import views, artikli_view, prodavnica_view, pretraga_view

urlpatterns = [
    path('', views.index, name='index'),
    path('kategorije/', views.lista_kategorija, name='lista_kategorija'),
    path('artikli/', artikli_view.lista_artikala, name='lista_artikala'),
    path('brisanje/artikla/<int:id>', artikli_view.brisanje_artikla, name='brisanje_artikla'),
    path('unos/artikla/', artikli_view.unos_artikla, name='unos_artikla'),
    path('unos/artikla/<int:id>', artikli_view.unos_artikla, name='unos_artikla_p'),
    path('prodavnice/', prodavnica_view.lista_prodavnica, name='lista_prodavnica'),
    path('brisanje/prodavnice/<int:id>', prodavnica_view.brisanje_prodavnice, name='brisanje_prodavnice'),
    path('unos/prodavnice/', prodavnica_view.unos_prodavnice, name='unos_prodavnice'),
    path('unos/prodavnice/<int:id>', prodavnica_view.unos_prodavnice, name='unos_prodavnice_p'),

    path('pretraga/artikli/', pretraga_view.pretraga_artikala, name='pretraga_artikala'),
    path('pretraga/artikli/naziv/', pretraga_view.pretraga_naziv, name='pretraga_naziv'),
    path('pretraga/artikli/opis_fraza/', pretraga_view.pretraga_opis_fraza, name='pretraga_opis_fraza'),
    path('pretraga/artikli/naziv_i_opis/', pretraga_view.pretraga_naziv_i_opis, name='pretraga_naziv_i_opis'),
    path('pretraga/artikli/naziv_ili_opis/', pretraga_view.pretraga_naziv_ili_opis, name='pretraga_naziv_ili_opis'),
    path('pretraga/artikli/cena/', pretraga_view.pretraga_cena, name='pretraga_cena'),
    path('pretraga/artikli/prodavnica/', pretraga_view.pretraga_prodavnica, name='pretraga_prodavnica')
]
