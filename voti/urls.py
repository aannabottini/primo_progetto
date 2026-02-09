from django.contrib import admin
#admin rappresenta la sezione di amministrazione del sito.
#indichiamo il prefisso dei nostri url.
from django.urls import path,include
from .views import index_voti
from .views import lista_materie
from .views import lista_voti
from .views import media_voti 
from .views import voto_max_min

app_name = 'voti'

urlpatterns = [
    path('', index_voti, name="index_voti"),
    path("lista_materie/", lista_materie, name="lista_materie"),
    path("lista_voti/", lista_voti, name="lista_voti"),
    path("media_voti/", media_voti, name="media_voti"),
    path("voto_max_min/", voto_max_min, name="voto_max_min"),
]