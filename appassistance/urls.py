from django.contrib import admin
from django.urls import path, include
#from user import views as user_view
from django.contrib.auth import views as auth

from appassistance import views as appassistance_view

urlpatterns = [
    path('', appassistance_view.index, name="index"), #esta era nuestra primera pagina
    path("trabajadores/", appassistance_view.trabajador, name="coder-trabajadores"),
    path("trabajadores/crear/", appassistance_view.creacion_trabajador, name="coder-trabajadores-crear"),
    # path("trabajadores/buscar/", appassistance_view.buscar_trabajadores, name="coder-trabajadores-buscar"),
    path("empresas/", appassistance_view.empresa, name="coder-empresas"),
    path("empresas/crear/", appassistance_view.creacion_empresas, name="coder-empresas-crear"),
    path("obras/", appassistance_view.obra, name="coder-obras"),
    path("obras/crear/", appassistance_view.creacion_obras, name="coder-obras-crear"),
    
    ##### user related path##########################
    #path('', include('user.urls')),
    path('login/', appassistance_view.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='appassistance/index.html'), name ='logout'),
    path('register/', appassistance_view.register, name ='register'),
]
