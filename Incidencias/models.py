from django.db import models
from Tecnico.models import Trabajador
from Activos.models import Activo


class Intervencion(models.Model):
    Codigo = models.IntegerField()
    FechaApertura = models.DateField(auto_created=True)
    FechaCierra = models.DateField(auto_created=False)
    TipoIntervencion = models.CharField(max_length=250)
    Descripcion = models.CharField(max_length=250)
    TecnicoAsignado = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    ActivoAsignado = models.ForeignKey(Activo, on_delete=models.CASCADE)
