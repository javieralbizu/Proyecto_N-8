from django.shortcuts import render


def inicio(request):
    return render(request, 'HTML/Pagina_Inicio.html')