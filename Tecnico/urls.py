from . import views
from django.urls import path

urlpatterns = [
    path('',views.CargarTabla, name='TablaTecnico'),
    path('NuevoTecnico/',views.NuevoTecnico, name='NuevoTecnico'),
    path('EditarTecnico/<int:id>',views.NuevoTecnico, name='EditarTecnico'),
    path('EliminarTecnico/<int:id>',views.EliminarTecnico, name='EliminarTecnico')
]