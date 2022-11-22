from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user        



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