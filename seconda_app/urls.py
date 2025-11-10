#Importiamo la funzione path da un modulo di django 
from django.urls import path
#Importiamo la funzione es_if dal file views.py
from seconda_app.views import es_if
#Importiamo la funzione if_else_elif dal file views.py
from seconda_app.views import if_else_elif
#Importiamo la funzione index_condizioni dal file views.py
from seconda_app.views import index_condizioni
#Importiamo la funzione es_for dal file views.py
from seconda_app.views import es_for


app_name = "seconda_app"
#Creiamo un vettore con tutti gli url della nostra applicazione.
urlpatterns = [
    #La funzione path definisce l’url
    #Il primo parametro rappresenta l’url(solo la parte dopo localhost:8000)
    # Il secondo parametro è la funzione da chiamare. 
    # Il terzo parametro è un nome che serve per identificare in modo univoco l’url nel server.
    path('index_condizioni', index_condizioni, name='index_condizioni'),
    path('es_if', es_if, name='es_if'),
    path('if_else_elif.html', if_else_elif, name='if_else_elif'),
    path('es_for.html', es_for, name='es_for')
]