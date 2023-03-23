from django.db import models

class Formulario(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    

class Estudiante(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    profesion=models.CharField(max_length=40)

class Entregable(models.Model):
    nombre=models.CharField(max_length=40)
    fecha_de_entrega=models.DateField()
    entregable=models.BooleanField()

class FamiliarUno(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.IntegerField()
    fecha_de_nac=models.DateField()
    def __str__(self):
        return self.nombre # de esta manera nos aparece por nombre en el django admin






# Create your models here.
