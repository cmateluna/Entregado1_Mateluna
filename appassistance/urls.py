from django.urls import path
from appassistance.views import *


urlpatterns = [
    path('', index, name="coder-inicio"), #esta era nuestra primera pagina
    path("trabajadores/", trabajador, name="coder-trabajadores"),
    path("trabajadores/crear/", creacion_trabajador, name="coder-trabajadores-crear"),
]
