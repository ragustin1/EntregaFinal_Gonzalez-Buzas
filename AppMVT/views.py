from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso, Profesor, Estudiante

# Create your views here.

def curso(request):
    
    curso=Curso(nombre="Curso de Python",comision=123456)
    
    curso.save()
   
    texto=f"Curso Creado: nombre: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)



def inicio(request):
    return render (request, "AppMVT/inicio.html")

def profesores(request):
    return render(request, "AppMVT/profesores.html" )

def estudiantes(request):
    return render(request, "AppMVT/estudiantes.html")

def entregables(request):
    return render(request, "AppMVT/entregables.html")