from django.urls import path
from . import views

app_name='inventario'

urlpatterns=[

    path('AgregarZapato',views.agregar_zapato,name='AgregarZapato'),
    path('VentaZapato',views.VentaZapato,name='VentaZapato')

]