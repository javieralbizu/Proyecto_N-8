from django import forms
from . import models

class ActivoForm(forms.ModelForm):
    class Meta:
        model = models.Activo
        fields = ['Codigo de Activacion','Nombre','Tipo de dispositivo','Modelo','Marca','Fecha de instalacion','Ubicacion','Estado operativo']
        widgets = { 
            'Codigo de Activacion' : forms.NumberInput(),
            'Nombre' : forms.TextInput(),
            'Tipo de dispositivo' : forms.TextInput(),
            'Modelo' : forms.TextInput(),
            'Marca' : forms.TextInput(),
            'Fecha de instalacion' : forms.DateInput(),
            'Ubicacion' : forms.TextInput(),
            'Estado operativo' : forms.CheckboxInput()
        }