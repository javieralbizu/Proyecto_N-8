from . import views
from django.urls import path

urlpatterns = [
    path('',views.TablaActivos, name='TablaActivos'),
    path('NuevoActivo/',views.NuevoActivo, name='NuevoActivo'),
    path('NuevoActivo/<int:id>/',views.NuevoActivo, name='EditarActivo'),
    path('EliminarActivo/<int:id>/',views.EliminarActivo, name='EliminarActivo')
]