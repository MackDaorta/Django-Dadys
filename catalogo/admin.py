from django.contrib import admin
#Importar el modelo Zapato
from .models import Zapato

#CRUD en el panel de administracion
admin.site.register(Zapato)
