from rest_framework import serializers 
from .models import Activo 

class ActivosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Activo
        fields=['CodigoActivacion','Nombre','TipoDispositivo','Modelo','Marca','FechaInstalacion','Ubicacion','EstadoOperativo']

