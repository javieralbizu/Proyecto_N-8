from . import views
from django.urls import path

urlpatterns = [
    path('Incidencias/', views.CargarTablaIncidencias, name='TablaIncidencias'),
    path('Incidencias/NuevaIncidencia/',views.NuevaIncidencia, name='IncidenciaNueva'),
    path('Incidencias/NuevaIncidencia/<int:id>',views.NuevaIncidencia, name='EditarIncidencia'),
    path('Incidencias/EliminarIncidencia/<int:id>',views.EliminarIncidencia, name='EliminarIncidencia')
]