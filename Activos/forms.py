from django import forms
from . import models

class ActivoForm(forms.ModelForm):
    class Meta:
        model = models.Activo
        fields = ['CodigoActivacion','Nombre','TipoDispositivo','Modelo','Marca','FechaInstalacion','Ubicacion','EstadoOperativo']
        widgets = { 
            'CodigoActivacion' : forms.NumberInput(),
            'Nombre' : forms.TextInput(),
            'TipoDispositivo' : forms.TextInput(),
            'Modelo' : forms.TextInput(),
            'Marca' : forms.TextInput(),
            'FechaInstalacion' : forms.DateInput(),
            'Ubicacion' : forms.TextInput(),
            'EstadoOperativo' : forms.CheckboxInput()
        }