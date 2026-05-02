from django import forms
from . import models

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = models.Trabajador
        fields = ['DNI', 'Nombre','Apellido', 'Email','Telefono']
        widgets = { 
            'DNI' : forms.TextInput(),
            'Nombre' : forms.TextInput(),
            'Apellido' : forms.TextInput(),
            'Email' : forms.EmailInput(),
            'Telefono' : forms.NumberInput()
        }

