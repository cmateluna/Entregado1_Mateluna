from django.shortcuts import render
from django.http import HttpResponse
from appassistance.models import Trabajadores, Empresa, Obra
from appassistance.forms import TrabajadoresFormulario, EmpresasFormulario, ObrasFormulario

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


def empresa(request):
    return render(request, "appassistance/empresas.html")


def creacion_empresas(request):

    if request.method == "POST":
     formulario = EmpresasFormulario(request.POST)

     if formulario.is_valid():
         # Accedemos al diccionario que contiene
         # la informacion del formulario
         data = formulario.cleaned_data

         empresas = Empresa(
             run=data["run"], nombre=data["nombre"], direccion=data["direccion"], email=data["email"])
         empresas.save()

    formulario = EmpresasFormulario()
    return render(request, "appassistance/empresas_formulario.html", {"formulario": formulario})


def obra(request):
    return render(request, "appassistance/obras.html")


def creacion_obras(request):

    if request.method == "POST":
     formulario = ObrasFormulario(request.POST)

     if formulario.is_valid():
         # Accedemos al diccionario que contiene
         # la informacion del formulario
         data = formulario.cleaned_data

         obras = Obra(
             nombre=data["nombre"], direccion=data["direccion"], email=data["email"], celular=data["celular"])
         obras.save()

    formulario = ObrasFormulario()
    return render(request, "appassistance/obras_formulario.html", {"formulario": formulario})
