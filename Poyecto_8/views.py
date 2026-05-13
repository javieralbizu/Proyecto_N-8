from django.shortcuts import render


def inicio(request):
    return render(request, 'HTML/Pagina_Inicio.html')

def login(request):
    return render(request,'HTML/Login.html')