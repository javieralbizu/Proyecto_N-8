from django.shortcuts import render

def CargarTablaIncidencias(request):
    return render(request, 'Incidencias/Tabla.html')
# Create your views here.
