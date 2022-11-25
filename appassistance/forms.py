from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']
            
