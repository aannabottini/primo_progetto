#Importiamo la funzione path da un modulo di django 
from django.urls import path
#Importiamo le funzioni dal file views.py
from api.views import todos_view
from api.views import spotify_view

app_name = "api"

urlpatterns = [
    #La funzione path definisce l’url
    #Il primo parametro rappresenta l’url(solo la parte dopo localhost:8000)
    # Il secondo parametro è la funzione da chiamare. 
    # Il terzo parametro è un nome che serve per identificare in modo univoco l’url nel server.
    path('todos/', todos_view, name='todos'),
    path('spotify/', spotify_view, name='spotify'),
]