#Importiamo la funzione path da un modulo di django 
from django.urls import path
#Importiamo la funzione es_if dal file views.py
from prova_pratica_0.views import indexProva
from prova_pratica_0.views import maxmin
from prova_pratica_0.views import media


app_name = "prova_pratica_0"
#Creiamo un vettore con tutti gli url della nostra applicazione.
urlpatterns = [
    #La funzione path definisce l’url
    #Il primo parametro rappresenta l’url(solo la parte dopo localhost:8000)
    # Il secondo parametro è la funzione da chiamare. 
    # Il terzo parametro è un nome che serve per identificare in modo univoco l’url nel server.
    path('', indexProva, name='view_a'), 
    path('maxmin', maxmin, name='maxmin'), 
    path('media', media, name='media'), 
]