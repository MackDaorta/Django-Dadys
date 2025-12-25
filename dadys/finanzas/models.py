from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Prestamo(models.Model):
    estados=[('P', 'Pendiente'),('C','Pagado'),('V','Vencido')]
    cliente=models.CharField(max_length=200)
    monto=models.DecimalField(max_digits=10,decimal_places=2)
    fecha_inicio=models.DateField(auto_now_add=True)
    fecha_vencimiento=models.DateField()
    estado=models.CharField(max_length=1,choices=estados,default='P')
    
    def esta_por_vencer(self):
        delta=self.fecha_vencimiento-timezone.now().date()
        return 0 <=delta.days<=3 and self.estado =='P'
    