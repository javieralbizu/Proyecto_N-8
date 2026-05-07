from .forms import TecnicoForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tecnico


def CargarTabla(request):
    tecnicos = Tecnico.objects.all()
    return render(request, "Tecnico/Tabla.html", {"lista": tecnicos})


def NuevoTecnico(request, id=None):
    if id:
        trabajador = get_object_or_404(Tecnico,id = id)
    else:
        trabajador = None

    if request.method == "POST":
        form = TecnicoForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect("TablaTecnico")

    else:
        form = TecnicoForm(instance=trabajador)
    return render(request, "Tecnico/NuevoTrabajador.html", {"form": form})

def EliminarTecnico(request, id):
    trabajador = get_object_or_404(Tecnico, id = id)
    trabajador.delete()
    return redirect('TablaTecnico')

