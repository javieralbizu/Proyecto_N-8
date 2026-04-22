from django.db import models

class Activo (models.Model):
    Codigo_de_activacion = models.BooleanField(default=False)
    Nombre = models.CharField(max_length=100)
    Tipo_de_dispositivo = models.CharField(max_length=200)
    Modelo = models.CharField(max_length=200)
    Marca = models.CharField(max_length=100)
    Fecha_instalacion = models.DateField(auto_now_add=True)
    Ubicacion = models.CharField(max_length=200)
    Estado_operativo = models.BooleanField(default=False)
