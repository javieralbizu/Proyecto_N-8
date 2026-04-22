from django.db import models

class Trabajador (models.Model):
    DNI = models.CharField(max_length=9)
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=40)
    Email = models.EmailField(unique = true)
    Telefono = models.CharField(max_length=15)