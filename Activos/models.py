from django.db import models

class Activo (models.Model):
    CodigoActivacion = models.IntegerField(default=False)
    Nombre = models.CharField(max_length=100)
    TipoDispositivo = models.CharField(max_length=200)
    Modelo = models.CharField(max_length=200)
    Marca = models.CharField(max_length=100)
    FechaInstalacion = models.DateField()
    Ubicacion = models.CharField(max_length=200)
    EstadoOperativo = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Marca} {self.Modelo}"


