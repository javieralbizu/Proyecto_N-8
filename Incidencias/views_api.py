from rest_framework import viewsets
from .models import Intervencion
from .serializers import IncidenciasSerializer


class IntervencionViewSet(viewsets.ModelViewSet):
    queryset = Intervencion.objects.all()
    serializer_class = IncidenciasSerializer
