from .forms import TrabajadorForm
from django.shortcuts import render, redirect
from .models import Trabajador

def CargarTabla(request):
    tecnicos = Trabajador.objects.all()
    return render(request, 'Tecnico/Tabla.html', {'lista': tecnicos})

def nuevo_trabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CargarTabla')
    else:
        form = TrabajadorForm()

    return render(request, 'Tecnico/nuevo_trabajador.html', {'form': form})
# Create your views here.
