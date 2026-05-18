from django.shortcuts import render, redirect, get_object_or_404
from .models import Activo
from .forms import ActivoForm

def TablaActivos(request):
    token = request.GET.get("token")
    Activos = Activo.objects.all()
    return render(request, 'Activos/Tabla.html', {'Activos': Activos, 'jwt_token':token})


def NuevoActivo(request, id=None):
    token = request.GET.get("token")
    if id:
        activo = get_object_or_404(Activo, id=id)
    else:
        activo = None

    if request.method == "POST":
        form = ActivoForm(request.POST, instance=activo)
        if form.is_valid():
            form.save()
            return redirect(f"/Activos/?token={token}")
    else:
        form = ActivoForm(instance=activo)
    return render(request, "Activos/NuevoActivo.html", {"form": form, "jwt_token":token})

def EliminarActivo(request, id):
    token = request.GET.get("token")
    activo = get_object_or_404(Activo, id = id)
    activo.delete()
    return redirect(f"/Activos/?token={token}")


