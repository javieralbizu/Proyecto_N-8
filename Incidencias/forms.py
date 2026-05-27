from django import forms
from . import models

class IntervencionForm(forms.ModelForm):
 
    TecnicoAsignado = forms.ModelChoiceField(
        queryset=models.Tecnico.objects.all(),
        empty_label="Seleccione un técnico",
        label="Tecnico Asignado"
    )

    ActivoAsignado = forms.ModelChoiceField(
        queryset=models.Activo.objects.all(),
        empty_label="Seleccione el activo",
        label="Activo Asignado"
        )
      
    class Meta:
        model = models.Intervencion
        fields = ['Codigo','FechaApertura','FechaCierre','TipoIntervencion','Descripcion','TecnicoAsignado','ActivoAsignado']
        labels = {'Codigo':'Código', 'FechaApertura':'Fecha de Apertura', 'FechaCierre':'Fecha de Cierre','Descripcion':'Descripción', 'TipoIntervencion': 'Tipo Intervencion'  }
        widgets = { 
            'Codigo' : forms.NumberInput(),
            'FechaApertura' : forms.DateInput(format='%Y-%m-%d',attrs={'type':'date'}),
            'FechaCierre' : forms.DateInput(format='%Y-%m-%d',attrs={'type':'date'}),
            'TipoIntervencion' : forms.TextInput(),
            'Descripcion' : forms.TextInput(),
        }