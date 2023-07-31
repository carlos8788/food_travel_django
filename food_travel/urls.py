from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('coordenadas', destinos_json, name='coordenadas'),
]
