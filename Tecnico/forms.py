from django import forms

class TrabajadorForm(forms.Form):
    DNI = forms.CharField(label="DNI", max_length=9)
    Nombre = forms.CharField(label="Nombre", max_length=30)
    Apellido = forms.CharField(label="Apellido", max_length=40)
    Email = forms.EmailField(label="Correo Electronico")
    Telefono = forms.CharField(label="Telefono")

