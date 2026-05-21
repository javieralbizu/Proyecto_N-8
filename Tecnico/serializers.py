from rest_framework import serializers 
from .models import Tecnico 

class TecnicosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tecnico
        fields=['DNI', 'Nombre', 'Apellido', 'Email', 'Telefono']

