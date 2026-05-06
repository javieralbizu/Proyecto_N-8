from django.shortcuts import render , redirect
from .forms import ActivoForm

def CargarTabla(request):
    return render(request, 'Activos/Tabla.html')

def NuevoActivo(request):
    if request.method == 'POST':
        form = ActivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CargarTabla')
        else:
            return render(request, 'Tecnico/NuevoActivo.html', {'form': form})
    else:  
        return render(request, 'Tecnico/NuevoActivo.html', {'form': ActivoForm()})
    
# Create your views here.
