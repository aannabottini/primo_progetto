#Importiamo la funzione path da un modulo di django 
from django.urls import path
#Importiamo la funzione homepage dal file views.py
from prima_app.views import homepage
#Importiamo la funzione welcome dal file views.py
from prima_app.views import welcome
#Importiamo la funzione lista dal file views.py
from prima_app.views import lista
#Importiamo la funzione chisiamo dal file views.py
from prima_app.views import chi_siamo

app_name = "prima_app"
#Creiamo un vettore con tutti gli url della nostra applicazione.
urlpatterns = [
    #La funzione path definisce l’url
    #Il primo parametro rappresenta l’url(solo la parte dopo localhost:8000)
    # Il secondo parametro è la funzione da chiamare. 
    # Il terzo parametro è un nome che serve per identificare in modo univoco l’url nel server.
    path('', homepage, name='homepage'), #http://localhost:8000/
    path('welcome', welcome, name='welcome'), #localhost:8000/welcome
    path('lista', lista, name="lista"), #localhost:8000/lista
    path('chi_siamo', chi_siamo, name="chi_siamo"), #localhost:8000/chi_siamo
]