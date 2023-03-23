from django.shortcuts import render
from Appcoder.models import Profesor,FamiliarUno
from django.http import HttpResponse
from django.template import Template, loader
import datetime
from .models import Formulario

# Create your views here.
def inicio(request):
    return render(request, 'Appcoder/inicio.html') #LISTO

def home(request):
    return render(request, 'Appcoder/home.html') #LISTO

def karen(request):
    return render(request, 'Appcoder/karen.html') #LISTO

def blog(request):
    return render(request,'Appcoder/blog.html') #LISTO

def about(request):
    return render(request,'Appcoder/about.html') #LISTO

def contact(request):

    if request.method == 'POST':
        datos=Formulario(nombre=request.POST['nombre'],apellido=request.POST['apellido'])
        datos.save()
    
    return render(request,'Appcoder/contact.html') #LISTO








