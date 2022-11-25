from appassistance.models import Trabajadores, Empresa, Obra
from appassistance.forms import TrabajadoresFormulario, EmpresasFormulario, ObrasFormulario
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


# def index(request):
#     return render(request, "appassistance/base.html")

##################################################################
####################index#######################################
def index(request):
    return render(request, 'appassistance/index.html',{'title':'index'})


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


def buscar_trabajadores(request):
    
    if request.GET:
        nombre_trabajador = request.GET.get("nombre_trabajador", "")
        if nombre_trabajador =="":
             trabajadores = []
        else:
            trabajadores = Trabajadores.objects.filter(nombre__icontains=nombre_trabajador)     
        return render(request, "appassistance/busqueda_trabajadores.html", {"listado_trabajador": trabajadores})
    
    return render(request, "appassistance/busqueda_trabajadores.html",{"listado_trabajador": []})    


#################### index#######################################
# def index(request):
#     return render(request, 'appassistance/index.html', {'title':'index'})
  
########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'appassistance/register.html', {'form': form, 'title':'register here'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'appassistance/login.html', {'form':form, 'title':'log in'})