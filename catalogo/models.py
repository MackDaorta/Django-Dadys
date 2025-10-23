from django.db import models

class Zapato(models.Model):

    #Codigo del Zapato
    modelo = models.CharField(max_length=50, unique=True, verbose_name='Modelo')

    #Marca del Zapato
    marca= models.CharField(max_length=20, verbose_name='Marca')

    #Precio de los zapatos
    precio= models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Precio')

    #Talla del zapato
    talla=models.FloatField(verbose_name='Talla')

    #Stock del zapato
    stock=models.PositiveSmallIntegerField(max_length=2,verbose_name='Stock')

    #Imagen del zapato
    imagen=models.ImageField(upload_to='zapatos/', blank=True, null=True, verbose_name='Imagen')

    def __str__(self):
        return f'{self.marca} - {self.modelo} (Talla {self.talla})'
