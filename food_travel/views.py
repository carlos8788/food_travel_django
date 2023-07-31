from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def destinos_json(request):
    destinos = list(DestinoCulinario.objects.values('nombre', 'ubicacion__latitud', 'ubicacion__longitud'))
    print(destinos)
    return JsonResponse(destinos, safe=False)
