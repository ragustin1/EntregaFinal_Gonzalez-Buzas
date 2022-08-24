from django.shortcuts import render
from django.http import HttpResponse
from AppMVT.models import *
from django.template import loader

# Create your views here.

def miPadre (self):
    
    padre = Padre(nombre = "Oscar", edad = 72, profesion = "Tornero")
    padre.save()
     
    dicc = {"nom": padre.nombre, "ed": padre.edad, "prof": padre.profesion}
    
    plantilla = loader.get_template('PlantillaPadre.html')
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def miMadre (self):
    
    madre = Madre(nombre = "Hilda", edad = 71, profesion = "Ama de casa")
    madre.save()
     
    dicc = {"nom": madre.nombre, "ed": madre.edad, "prof": madre.profesion}
    
    plantilla = loader.get_template('PlantillaMadre.html')
    documento = plantilla.render(dicc)
    return HttpResponse(documento)
      

def miNovia (self):
    
    novia = Novia(nombre = "Nadia", edad = 29, profesion = "Cirujana")
    novia.save()
    
    dicc = {"nom": novia.nombre, "ed": novia.edad, "prof": novia.profesion}
    
    plantilla = loader.get_template('PlantillaNovia.html')
    documento = plantilla.render(dicc)
    return HttpResponse(documento)