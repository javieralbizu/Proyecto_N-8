from . import views
from django.urls import path

urlpatterns = [
    path('Activos/',views.TablaActivos, name='TablaActivos'),
    path('Activos/NuevoActivo/',views.NuevoActivo, name='NuevoActivo'),
    path('Activos/NuevoActivo/<int:id>/',views.NuevoActivo, name='EditarActivo'),
    path('Activos/EliminarActivo/<int:id>/',views.EliminarActivo, name='EliminarActivo')
]