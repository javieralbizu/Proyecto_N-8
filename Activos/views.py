from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Activo
from .forms import ActivoForm

def TablaActivos(request):
    token = request.GET.get("token", "")
    terminoBusqueda = request.GET.get('buscar', '')

    if terminoBusqueda:
        activos_list = Activo.objects.filter(Nombre__icontains=terminoBusqueda).order_by('CodigoActivacion')
    else:
        activos_list = Activo.objects.all().order_by('CodigoActivacion')

    paginator = Paginator(activos_list, 8)
    numero_pagina = request.GET.get("page")
    activos_paginados = paginator.get_page(numero_pagina)
    
    return render(request, 'Activos/Tabla.html', {
        'Activos': activos_paginados, 
        'jwt_token': token,
        'busqueda': terminoBusqueda
    })


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


