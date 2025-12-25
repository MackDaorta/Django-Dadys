from django import forms
from .models import Zapato, Marca

class ZapatoForm(forms.ModelForm):
    class Meta:
        model = Zapato
        fields = ['nombre', 'marca', 'precio', 'imagen'] 
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Doble Evilla'}),
            'marca': forms.Select(attrs={'class': 'form-select'}), 
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }