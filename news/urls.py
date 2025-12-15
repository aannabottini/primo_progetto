#Importiamo la funzione path da un modulo di django 
from django.urls import path

from .views import home
from .views import articoloDetailView

app_name = "news"
#Creiamo un vettore con tutti gli url della nostra applicazione.
urlpatterns = [
    #La funzione path definisce l’url
    #Il primo parametro rappresenta l’url(solo la parte dopo localhost:8000)
    # Il secondo parametro è la funzione da chiamare. 
    # Il terzo parametro è un nome che serve per identificare in modo univoco l’url nel server.
    path('', home, name='news'),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
]