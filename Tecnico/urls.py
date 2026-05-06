from . import views
from django.urls import path

urlpatterns = [
    path('Tecnico/',views.CargarTabla, name='CargarTabla'),
    path('Tecnico/Nuevo/',views.NuevoTrabajador, name='NuevoTrabajador'),
    path('Tecnico/Nuevo/<int:id>',views.NuevoTrabajador, name='EditarTrabajador'),
    path('Tecnico/EliminarTrabajador/<int:id>',views.EliminarTecnico, name='EliminarTrabajador')
]