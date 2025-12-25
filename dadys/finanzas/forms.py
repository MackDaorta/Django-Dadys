from django import forms
from datetime import date
from .models import *

class PrestamoForm(forms.ModelForm):
    class Meta:
        model=Prestamo
        fields=['estado','cliente','monto','fecha_vencimiento']

        widgets={
            'estado': forms.ChoiceField(attrs={
                'class': 'form-control',
                'placeholder': 'Elige un estado'
            }),
            'cliente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del prestamista'
            }),
            'monto': forms.FloatField(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la cantidad a pagar 0.00'
            }),
            'fecha_vencimiento': forms.DateInput(attrs={
                'class': 'form-control',
            }),
        }

        def clean_cliente(self):
            cliente= self.cleaned_data.get('cliente')
            if cliente and len(cliente)<5:
                raise forms.ValidationError('El cliente debe tener un nombre mayor a 5')
            return cliente
        
        def clean_vencimiento(self):
            vencimiento=self.cleaned_data.get('fecha_vencimiento')
            if vencimiento and vencimiento<date.today():
                raise forms.ValidationError('la fecha no puede ser anterior al prestamo')
            return vencimiento 