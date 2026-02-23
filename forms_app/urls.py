from django.contrib import admin
from django.urls import path,include

from forms_app.views import contatto

app_name = 'forms_app'

urlpatterns = [
    path('contattaci/', contatto , name="contattaci"),

]