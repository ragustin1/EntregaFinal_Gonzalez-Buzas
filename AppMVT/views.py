from django.http import HttpResponse
from django.shortcuts import render
from .models import Entrenador, Persona, Ruta
from .forms import RutaFormulario


# Create your views here.

def inicio(request):
    return render (request, "AppMVT/inicio.html")

def personas(request):
    return render(request, "AppMVT/personas.html" )

def entrenadores(request):
    return render(request, "AppMVT/entrenadores.html")

def rutas(request):
    return render(request, "AppMVT/rutas.html")

# def rutaFormulario(request):
#     if request.method == "POST":
#         miFormulario = RutaFormulario(request.POST)
#         print (miFormulario)
#         if miFormulario.is_valid:
#             informacion = miFormulario.cleaned_data
#             rutaNueva= Ruta (nombre = informacion['rutaNueva'])
#             rutaNueva.save()
#             return render (request, "AppMVT/inicio.html")
#     else:  
#             miFormulario = RutaFormulario()
#     return render(request, "AppMVT/rutaFormulario.html", {"miFormulario":miFormulario})



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



def busquedaRuta (request):
    return render (request, "AppMVT/busquedaRuta.html")

def buscar(request):
    if request.GET ["ubicacion"]:
    
    # respuesta = f"Estoy buscando la ruta N° {request.GET['ruta']}"
        ubicacion = request.GET['ubicacion']
        ubicacionRuta = Ruta.objects.filter(ubicacion=ubicacion)
    
        return render (request, "AppMVT/busquedaRuta.html",{"rutas":ubicacionRuta, "ubicacion":ubicacion})
    
    else:
        
        respuesta = "No enviaste datos"
        
    return  HttpResponse(respuesta)
    
    