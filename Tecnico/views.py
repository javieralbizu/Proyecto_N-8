from .forms import TrabajadorForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Trabajador


def CargarTabla(request):
    tecnicos = Trabajador.objects.all()
    return render(request, "Tecnico/Tabla.html", {"lista": tecnicos})


def NuevoTrabajador(request, id=None):
    if id:
        trabajador = get_object_or_404(Trabajador,id = id)
    else:
        trabajador = None

    if request.method == "POST":
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect("CargarTabla")

    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, "Tecnico/NuevoTrabajador.html", {"form": form})

def EliminarTecnico(request, id):
    trabajador = get_object_or_404(Trabajador,id = id)
    trabajador.delete()
    return redirect('CargarTabla')

