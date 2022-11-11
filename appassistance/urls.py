from django.urls import path
from appassistance.views import *

urlpatterns = [
    path("inicio/", inicio, name="coder-inicio"), #esta era nuestra primera pagina
]
