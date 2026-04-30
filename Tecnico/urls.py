from . import views
from django.urls import path

urlpatterns = [
    path('',views.CargarTabla, name='CargarTabla'),
    path('nuevo/',views.nuevo_trabajador, name='nuevo_trabajador')
]