from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    proveedor = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Zapato(models.Model):
    nombre = models.CharField(max_length=60)
    marca = models.ForeignKey(Marca, null=True, blank=True, related_name="zapatos", on_delete=models.CASCADE)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='zapatos/')
    
    @property
    def stock_total(self):
        return sum(talla.stock for talla in self.tallas.all())

    def __str__(self):
        return f"{self.nombre} - {self.marca}"

class VariacionTalla(models.Model):
    zapato = models.ForeignKey(Zapato, related_name='tallas', on_delete=models.CASCADE)
    talla = models.PositiveIntegerField() # Ejemplo: 38, 40, 42
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.zapato.nombre} - Talla: {self.talla}"