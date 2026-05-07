from django.shortcuts import render, redirect, get_object_or_404
from .models import Activo
from .forms import ActivoForm

def TablaActivos(request):
    Activos = Activo.objects.all()
    return render(request, 'Activos/Tabla.html', {'Activos': Activos})


def NuevoActivo(request, id=None):
    if id:
        activo = get_object_or_404(Activo, id=id)
    else:
        activo = None

    if request.method == "POST":
        form = ActivoForm(request.POST, instance=activo)
        if form.is_valid():
            form.save()
            return redirect("TablaActivos")
    else:
        form = ActivoForm(instance=activo)
    return render(request, "Activos/NuevoActivo.html", {"form": form})

def EliminarActivo(request, id):
    activo = get_object_or_404(Activo, id = id)
    activo.delete()
    return redirect('TablaActivos')


