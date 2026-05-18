from .forms import TecnicoForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tecnico


def CargarTabla(request):
    token = request.GET.get("token")
    tecnicos = Tecnico.objects.all()
    return render(request, "Tecnico/Tabla.html", {"lista": tecnicos, "jwt_token":token})


def NuevoTecnico(request, id=None):
    token = request.GET.get("token")
    if id:
        trabajador = get_object_or_404(Tecnico,id = id)
    else:
        trabajador = None

    if request.method == "POST":
        form = TecnicoForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect(f"/Tecnico/?token={token}")

    else:
        form = TecnicoForm(instance=trabajador)
    return render(request, "Tecnico/NuevoTrabajador.html", {"form": form, "jwt_token": token})

def EliminarTecnico(request, id):
    token = request.GET.get("token")
    trabajador = get_object_or_404(Tecnico, id = id)
    trabajador.delete()
    return redirect(f"/Tecnico/?token={token}")

