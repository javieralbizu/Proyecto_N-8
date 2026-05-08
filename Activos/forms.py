from django import forms
from . import models

class ActivoForm(forms.ModelForm):
    class Meta:
        model = models.Activo
        fields = ['CodigoActivacion','Nombre','TipoDispositivo','Modelo','Marca','FechaInstalacion','Ubicacion','EstadoOperativo']
        labels= {'CodigoActivacion':'Codigo de Activacion', 'TipoDispositivo':'Tipo de Dispositivo', 
                 'FechaInstalacion':'Fecha de Instalacion','EstadoOperativo':'Operativo'}
        widgets = { 
            'CodigoActivacion' : forms.NumberInput(),
            'Nombre' : forms.TextInput(),
            'TipoDispositivo' : forms.TextInput(),
            'Modelo' : forms.TextInput(),
            'Marca' : forms.TextInput(),
            'FechaInstalacion' : forms.DateInput(format='%Y-%m-%d',attrs= {'type': 'date'}),
            'Ubicacion' : forms.TextInput(),
            'EstadoOperativo' : forms.CheckboxInput()
        }