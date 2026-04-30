from . import views
from django.urls import path

urlpatterns = [
    path('Tecnico/',views.CargarTabla)
]