from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class DestinoCulinario(models.Model):
    
    nombre = models.CharField(max_length=255)
    tipo_cocina = models.CharField(max_length=255)
    ingredientes = models.CharField(max_length=255, blank=True)
    precio_minimo = models.FloatField()
    precio_maximo = models.FloatField()
    popularidad = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    ubicacion = models.ForeignKey('Ubicacion', on_delete=models.CASCADE)
    imagen = models.URLField(blank=True)


class Actividad(models.Model):
    
    nombre = models.CharField(max_length=255)
    destino = models.ForeignKey('DestinoCulinario', on_delete=models.CASCADE)
    hora_inicio = models.DateTimeField(default=timezone.now)

class RutaVisita(models.Model):
    
    nombre = models.CharField(max_length=255)
    destinos = models.ManyToManyField('DestinoCulinario')


class Ubicacion(models.Model):

    direccion = models.CharField(max_length=255)
    latitud = models.CharField(max_length=255)
    longitud = models.CharField(max_length=255)
    

class Usuario(User):
    historial_rutas = models.ManyToManyField('RutaVisita', blank=True)

class Review(models.Model):
    
    destino = models.ForeignKey('DestinoCulinario', on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentario = models.TextField()
    animo_choices = [
        ('Positivo', 'Positivo'),
        ('Negativo', 'Negativo'),
    ]
    animo = models.CharField(max_length=8, choices=animo_choices)

