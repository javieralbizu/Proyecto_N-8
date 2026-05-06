from . import views
from django.urls import path

urlpatterns = [
    path('Activos/',views.CargarTabla),
    path('Activos/NuevoActivo/',views.NuevoActivo)
]