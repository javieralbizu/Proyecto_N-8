from django.db import models

class Tecnico (models.Model):
    DNI = models.CharField(max_length=9)
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=40)
    Email = models.EmailField()
    Telefono = models.IntegerField()

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"