from django.shortcuts import render , redirect, get_object_or_404
from .forms import IntervencionForm
from .models import Intervencion

def CargarTablaIncidencias(request):
    intervenciones = Intervencion.objects.all()
    return render(request, 'Incidencias/Tabla.html',{'Incidencias':intervenciones} )

def NuevaIncidencia(request, id=None):
    if id:
        incidencia = get_object_or_404(Intervencion,id=id)
    else:
        incidencia= None

    if request.method == 'POST':
        form = IntervencionForm(request.POST, instance=incidencia)
        if form.is_valid():
            form.save()
            return redirect('TablaIncidencias')
            
    else: 
        form = IntervencionForm(instance=incidencia)

    return render(request, 'Incidencias/NuevaIncidencia.html', {'form': form})

def EliminarIncidencia(request, id):
    incidencia = get_object_or_404(Intervencion,id=id)
    incidencia.delete()
    return redirect('TablaIncidencias')

