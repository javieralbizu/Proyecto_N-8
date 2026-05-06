from django.shortcuts import render , redirect
from .forms import IntervencionForm

def CargarTablaIncidencias(request):
    return render(request, 'Incidencias/Tabla.html')

def NuevaIncidencia(request):
    if request.method == 'POST':
        form = IntervencionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CargarTabla')
        else:
            return render(request, 'Incidencias/NuevaIncidencia.html', {'form': form})
    else:  
        return render(request, 'Incidencias/NuevaIncidencia.html', {'form': IntervencionForm()})
# Create your views here.
