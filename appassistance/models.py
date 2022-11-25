from django.db import models


# Create your models here.

class Trabajadores(models.Model):
    run = models.IntegerField()
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    edad = models.IntegerField()
    email = models.EmailField()
    
class Empresa(models.Model):
    run = models.IntegerField()    
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    email = models.EmailField()
    

class Obra(models.Model):
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    email = models.EmailField()
    celular = models.IntegerField()    
    
