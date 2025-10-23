from django.shortcuts import render
from .models import Zapato

def home(request):
    #obtener todos los zapatos de la base de datos
    zapatos = Zapato.objects.all()

    #crear diccionario para enviar al HTML
    context ={
        'lista_zapatos':zapatos
    }
    #renderizamos el archivo HTML y le damos el diccionario
    return render(request, 'catalogo/home.html', context)
    