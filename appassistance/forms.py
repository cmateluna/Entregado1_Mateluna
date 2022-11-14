from django import forms


class TrabajadoresFormulario(forms.Form):
    #Especificar los campos
    run = forms.IntegerField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
