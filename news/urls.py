#Importiamo la funzione path da un modulo di django 
from django.urls import path

from .views import home
from .views import articoloDetailView
from .views import lista_articoli
from .views import queryBase

app_name = "news"
#Creiamo un vettore con tutti gli url della nostra applicazione.
urlpatterns = [
    #La funzione path definisce l’url
    #Il primo parametro rappresenta l’url(solo la parte dopo localhost:8000)
    # Il secondo parametro è la funzione da chiamare. 
    # Il terzo parametro è un nome che serve per identificare in modo univoco l’url nel server.
    path('', home, name='homepage'),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>", lista_articoli, name="lista_articoli"),
    path("lista_articoli/", lista_articoli, name="lista_articoli"),
    path("query_base/", queryBase, name="query_base")
]