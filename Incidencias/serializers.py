from rest_framework import serializers 
from .models import Intervencion 
from Activos.models import Activo
from Tecnico.models import Tecnico
from Activos.serializers import ActivosSerializer
from Tecnico.serializers import TecnicosSerializer

class IncidenciasSerializer(serializers.ModelSerializer):
    activo = ActivosSerializer(read_only=True, source='ActivoAsignado')
    tecnico = TecnicosSerializer(read_only = True, source='TecnicoAsignado')
    """
    activo_id = serializers.PrimaryKeyRelatedField(
        queryset= Activo.objects.all(),
        source="ActivoAsignado",
        write_only = True
    )
   """
    """
    tecnico_id = serializers.PrimaryKeyRelatedField(
        queryset= Tecnico.objects.all(),
        source="TecnicoAsignado",
        write_only = True
    )
 """

    class Meta:
        model=Intervencion
        fields=['Codigo','FechaApertura','FechaCierre','TipoIntervencion','Descripcion','ActivoAsignado','TecnicoAsignado','tecnico','activo']