from . import views
from django.urls import path

urlpatterns = [
    path('', views.CargarTablaIncidencias, name='TablaIncidencias'),
    path('NuevaIncidencia/',views.NuevaIncidencia, name='IncidenciaNueva'),
    path('NuevaIncidencia/<int:id>',views.NuevaIncidencia, name='EditarIncidencia'),
    path('EliminarIncidencia/<int:id>',views.EliminarIncidencia, name='EliminarIncidencia')
]