from django.contrib import admin
from django.urls import path,include

from forms_app.views import index_contatti
from forms_app.views import contatto
from forms_app.views import lista_contatti

app_name = 'forms_app'

urlpatterns = [
    path('', index_contatti, name="index_contatti"),
    path('contattaci/', contatto , name="contattaci"),
    path('lista_contatti/', lista_contatti, name="lista_contatti"),
]