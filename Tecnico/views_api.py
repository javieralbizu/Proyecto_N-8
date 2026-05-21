from rest_framework import viewsets 
from .models import Tecnico
from .serializers import  TecnicosSerializer

class TecnicoViweSet(viewsets.ModelViewSet):
    
    queryset = Tecnico.objects.all()    
    serializer_class = TecnicosSerializer