from django.db import models

class Activo (models.Model):
    CodigoActivacion = models.BooleanField(default=False)
    Nombre = models.CharField(max_length=100)
    TipoDispositivo = models.CharField(max_length=200)
    Modelo = models.CharField(max_length=200)
    Marca = models.CharField(max_length=100)
    FechaInstalacion = models.DateField(auto_now_add=True)
    Ubicacion = models.CharField(max_length=200)
    EstadoOperativo = models.BooleanField(default=False)
