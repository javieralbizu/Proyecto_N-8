from . import views
from django.urls import path

urlpatterns = [
    path('Tecnico/',views.CargarTabla, name='CargarTabla'),
    path('Tecnico/Nuevo/',views.NuevoTrabajador, name='NuevoTrabajador')
]