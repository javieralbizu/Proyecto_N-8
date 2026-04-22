from django.db import models
from Tecnico.models import Trabajador
from Activos.models import Activo


class Intervencion(models.Model):
    Codigo = models.IntegerField()
    Fecha_de_apertura = models.DateField(auto_created=True)
    Fecha_de_cierra = models.DateField(auto_created=False)
    Tipo_de_intervencion = models.CharField(max_length=250)
    Descripcion = models.CharField(max_length=250)
    Tecnico_asignado = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    Activo_asignado = models.ForeignKey(Activo, on_delete=models.CASCADE)
