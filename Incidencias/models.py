from django.db import models
from Tecnico.models import Tecnico
from Activos.models import Activo


class Intervencion(models.Model):
    Codigo = models.IntegerField()
    FechaApertura = models.DateField()
    FechaCierre = models.DateField()
    TipoIntervencion = models.CharField(max_length=250)
    Descripcion = models.CharField(max_length=250)
    TecnicoAsignado = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    ActivoAsignado = models.ForeignKey(Activo, on_delete=models.CASCADE)
