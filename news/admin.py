from django.contrib import admin
from .models import Articolo, Giornalista
# registrare le due classi nel pannello di amministrazione:
admin.site.register(Articolo)
admin.site.register(Giornalista)