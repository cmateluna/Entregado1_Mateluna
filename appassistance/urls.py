from django.urls import path
from appassistance.views import *


urlpatterns = [
    path('', index, name="coder-inicio"), #esta era nuestra primera pagina
    path("trabajadores/", trabajador, name="coder-trabajadores"),
    path("trabajadores/crear/", creacion_trabajador, name="coder-trabajadores-crear"),
    path("empresas/", empresa, name="coder-empresas"),
    path("empresas/crear/", creacion_empresas, name="coder-empresas-crear"),
    path("obras/", obra, name="coder-obras"),
    path("obras/crear/", creacion_obras, name="coder-obras-crear"),
]
