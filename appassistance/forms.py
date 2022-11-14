from django import forms


class TrabajadoresFormulario(forms.Form):
    #Especificar los campos
    run = forms.IntegerField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()

class EmpresasFormulario(forms.Form): 
    run = forms.IntegerField()    
    nombre = forms.CharField()
    direccion = forms.CharField()
    email = forms.EmailField()

class ObrasFormulario(forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField()
    email = forms.EmailField()
    celular = forms.IntegerField() 