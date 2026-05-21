from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.CargarTablaIncidencias, name='TablaIncidencias'),
    path('NuevaIncidencia/',views.NuevaIncidencia, name='IncidenciaNueva'),
    path('EditarIncidencia/<int:id>',views.NuevaIncidencia, name='EditarIncidencia'),
    path('EliminarIncidencia/<int:id>',views.EliminarIncidencia, name='EliminarIncidencia'),
    path('api/', include('Incidencias.api_urls'))
]