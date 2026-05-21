from rest_framework import viewsets 
from .models import Activo
from .serializers import  ActivosSerializer

class ActivoViweSet(viewsets.ModelViewSet):
    
    queryset = Activo.objects.all()    
    serializer_class = ActivosSerializer