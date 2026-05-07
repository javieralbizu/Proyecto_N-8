from django import forms
from . import models

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = models.Tecnico
        fields = ['DNI', 'Nombre','Apellido', 'Email','Telefono']
        widgets = { 
            'DNI' : forms.TextInput(),
            'Nombre' : forms.TextInput(),
            'Apellido' : forms.TextInput(),
            'Email' : forms.EmailInput(),
            'Telefono' : forms.NumberInput()
        }

