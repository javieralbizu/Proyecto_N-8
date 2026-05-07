from . import views
from django.urls import path

urlpatterns = [
    path('',views.CargarTabla, name='CargarTabla'),
    path('Nuevo/',views.NuevoTrabajador, name='NuevoTrabajador'),
    path('Nuevo/<int:id>',views.NuevoTrabajador, name='EditarTrabajador'),
    path('EliminarTrabajador/<int:id>',views.EliminarTecnico, name='EliminarTrabajador')
]