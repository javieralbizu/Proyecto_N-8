from .forms import TrabajadorForm
from django.shortcuts import render, redirect
from .models import Trabajador

def CargarTabla(request):
    tecnicos = Trabajador.objects.all()
    return render(request, 'Tecnico/Tabla.html', {'lista': tecnicos})

def NuevoTrabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CargarTabla')
        else:
            return render(request, 'Tecnico/NuevoTrabajador.html', {'form': form})
    else:  
        return render(request, 'Tecnico/NuevoTrabajador.html', {'form': TrabajadorForm()})

