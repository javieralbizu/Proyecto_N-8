from django.shortcuts import render , redirect, get_object_or_404
from .forms import IntervencionForm
from .models import Intervencion

def CargarTablaIncidencias(request):
    token = request.GET.get("token")
    intervenciones = Intervencion.objects.all()
    return render(request, 'Incidencias/Tabla.html',{'Incidencias':intervenciones, "jwt_token":token} )

def NuevaIncidencia(request, id=None):
    token = request.GET.get("token")
    if id:
        incidencia = get_object_or_404(Intervencion,id=id)
    else:
        incidencia= None

    if request.method == 'POST':
        form = IntervencionForm(request.POST, instance=incidencia)
        if form.is_valid():
            form.save()
            return redirect(f"/Incidencias/?token={token}")
            
    else: 
        form = IntervencionForm(instance=incidencia)

    return render(request, 'Incidencias/NuevaIncidencia.html', {'form': form, 'jwt_token': token})

def EliminarIncidencia(request, id):
    token = request.GET.get("token")
    incidencia = get_object_or_404(Intervencion,id=id)
    incidencia.delete()
    return redirect(f"/Incidencias/?token={token}")

