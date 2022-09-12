from django.http import HttpResponse
from django.shortcuts import render
from .models import Entrenador, Persona, Ruta
from .forms import RutaFormulario, PersonaFormulario, EntrenadorFormulario


# Create your views here.

def inicio(request):
    return render (request, "AppMVT/inicio.html")

# def personas(request):
#     return render(request, "AppMVT/personas.html" )

def personas(request):
    personas=Persona.objects.all()
    print(personas)
    return render(request, "AppMVT/personas.html", {"personas":personas})

def entrenadores(request):
    entrenadores=Entrenador.objects.all()
    print(entrenadores)
    return render(request, "AppMVT/entrenadores.html", {"entrenadores":entrenadores})

def rutas(request):
    rutas=Ruta.objects.all()
    print(rutas)
    return render(request, "AppMVT/rutas.html", {"rutas":rutas})

def rutaFormulario(request):

    if request.method=="POST":
        miFormulario= RutaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            print(info)
            rutaNueva=Ruta(nombre=info['nombre'],ubicacion=info['ubicacion'],longitud=info['longitud'],vigencia=info['vigencia'])
            rutaNueva.save()
            return render(request, "AppMVT/inicio.html")    
    else:
        miFormulario=RutaFormulario()
    return render(request, "AppMVT/rutaFormulario.html", {"miFormulario":miFormulario})

def personaFormulario(request):

    if request.method=="POST":
        miFormulario= PersonaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            print(info)
            personaNueva=Persona(nombre=info['nombre'],apellido=info['apellido'],edad=info['edad'],
            ubicacion=info['ubicacion'],email=info['email'])
            personaNueva.save()
            return render(request, "AppMVT/inicio.html")    
    else:
        miFormulario=PersonaFormulario()
    return render(request, "AppMVT/personaFormulario.html", {"miFormulario":miFormulario})

def entrenadorFormulario(request):

    if request.method=="POST":
        miFormulario= EntrenadorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            print(info)
            entrenadorNuevo=Entrenador(nombre=info['nombre'],apellido=info['apellido'],edad=info['edad'],
            ubicacion=info['ubicacion'],nivel=info['nivel'],email=info['email'])
            entrenadorNuevo.save()
            return render(request, "AppMVT/inicio.html")    
    else:
        miFormulario=EntrenadorFormulario()
    return render(request, "AppMVT/entrenadorFormulario.html", {"miFormulario":miFormulario})



def busquedaRuta (request):
    return render (request, "AppMVT/busquedaRuta.html")

def buscar(request):
    if request.GET ["ubicacion"]:
    
        ubicacion = request.GET['ubicacion']
        ubicacionRuta = Ruta.objects.filter(ubicacion=ubicacion)
    
        return render (request, "AppMVT/busquedaRuta.html",{"rutas":ubicacionRuta, "ubicacion":ubicacion})
    
    else:
        
        respuesta = "No enviaste datos"
        
    return  HttpResponse(respuesta)
    
    