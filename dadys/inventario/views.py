from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import Zapato, VariacionTalla
from .forms import *

def agregar_zapato(request):
    TallaFormSet = inlineformset_factory(
        Zapato, VariacionTalla, 
        fields=('talla', 'stock'), 
        extra=3,  
        can_delete=True
    )

    if request.method == 'POST':
        form = ZapatoForm(request.POST, request.FILES)
        formset = TallaFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            zapato = form.save()
            formset.instance = zapato 
            formset.save()
            return redirect('lista_zapatos')
    else:
        form = ZapatoForm()
        formset = TallaFormSet()

    return render(request, 'AgregarZapato.html', {
        'form': form,
        'formset': formset
    })

def VentaZapato(request):
    lista=Zapato.objects.all()
    return render(request,'VentaZapato.html',{
        "lista":lista,
    })

def AgregarMarca(request):
    lista=Marca.objects.all()
    if request.method == 'POST':
        form= MarcaForm(request.POST)
        
        if form.is_valid():
            marca=form.save()
            return redirect('lista_zapatos')
    else:
        form= MarcaForm()
    return render(request,'AgregarMarca.html',{
        'lista':lista,
        'form':form
    })