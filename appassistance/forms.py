from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TrabajadoresFormulario(forms.Form):
    #Especificar los campos
    run = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.CharField()
    email = forms.EmailField()

class EmpresasFormulario(forms.Form): 
    run = forms.CharField()    
    nombre = forms.CharField()
    direccion = forms.CharField()
    email = forms.EmailField()

class ObrasFormulario(forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField()
    email = forms.EmailField()
    celular = forms.IntegerField() 

class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField()
    email = forms.EmailField()
    phone_no = forms.CharField()
    first_name = forms.CharField()   
    last_name = forms.CharField()
    password1: forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']
            

