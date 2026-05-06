from django import forms
from . import models

class IntervencionForm(forms.ModelForm):
    TecnicoAsignado = forms.ModelChoiceField(
        queryset=models.Trabajador.objects.all(),
        empty_label="Seleccione un técnico"
    )
    
    ActivoAsignado = forms.ModelChoiceField(
        queryset=models.Activo.objects.all(),
        empty_label="Seleccione el activo"
        )
    class Meta:
        model = models.Intervencion
        fields = ['Codigo','FechaApertura','FechaCierra','TipoIntervencion','Descripcion','TecnicoAsignado','ActivoAsignado']
        widgets = { 
            'Codigo' : forms.NumberInput(),
            'FechaApertura' : forms.DateInput(),
            'FechaCierra' : forms.DateInput(),
            'TipoIntervencion' : forms.TextInput(),
            'Descripcion' : forms.TextInput(),
        }