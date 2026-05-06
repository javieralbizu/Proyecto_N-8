from . import views
from django.urls import path

urlpatterns = [
    path('Incidencias/', views.CargarTablaIncidencias),
    path('Incidencias/NuevaIncidencia/',views.NuevaIncidencia)
]