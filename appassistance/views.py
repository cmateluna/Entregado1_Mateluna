from django.shortcuts import render
from django.http import HttpResponse
from appassistance.models import Trabajadores
from appassistance.forms import TrabajadoresFormulario

# Create your views here.

def index(request):
    
    return render(request, "appassistance/base.html")


def trabajador(request):
    return render(request, "appassistance/trabajadores.html")


def creacion_trabajador(request):
    
    if request.method == "POST":
     formulario = TrabajadoresFormulario(request.POST)
      
     if formulario.is_valid():
            # Accedemos al diccionario que contiene
            # la informacion del formulario
           data = formulario.cleaned_data
             
           trabajadores = Trabajadores(run=data["run"], nombre=data["nombre"], apellido=data["apellido"], edad=data["edad"], email=data["email"])
           trabajadores.save()
        
    formulario = TrabajadoresFormulario()    
    return render(request, "appassistance/trabajadores_formulario.html", {"formulario":formulario})