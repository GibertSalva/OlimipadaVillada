from django.shortcuts import render
from .models import *

# Create your views here.
def registro_entradas(request):
    obj = Entrada.objects.all
    context = {
        'hora_entrada': obj.hora_entrada,
        'sucursal': obj.sucursal    
    }
    return render(request, "Detector/templates/index.html", context)