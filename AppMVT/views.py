from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Avatar
from .forms import UserRegisterForm, UserEditForm, AvatarForm, CommentForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

#@login_required
def inicio(request):
    # Agregamos los objetos de Post
    avatares = Avatar.objects.filter(user=request.user.id)
    posts = Post.objects.all()
    if len(avatares) == 0:
        return render (request, "AppMVT/inicio.html", {'posts':posts})
    else:
        return render (request, "AppMVT/inicio.html", {'posts':posts, 'url':avatares[0].imagen.url}) 
    
    
def about(request):
    return render(request, "AppMVT/about.html")
    

# Ahora agregamos la vista detallada del POST

def postDetalle(request, slug):
    avatares = Avatar.objects.filter(user=request.user.id)
    post = Post.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                
                return redirect('postDetalle', slug=post.slug)
                                
    else:
        form = CommentForm()
    if len(avatares) == 0:
        return render (request, "AppMVT/postDetalle.html", {'post':post, 'form':form,})
    else:
        return render (request, "AppMVT/postDetalle.html", {'post':post, 'form':form, 'url':avatares[0].imagen.url}) 
   
   
   
def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST )
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                avatares = Avatar.objects.filter(user=request.user.id)
                posts = Post.objects.all()
                if len(avatares) == 0:
                        return render (request, "AppMVT/inicio.html", {'posts':posts})
                else:
                        return render (request, "AppMVT/inicio.html", {'posts':posts, 'url':avatares[0].imagen.url}) 
                
            else:
                return render(request, 'AppMVT/login.html', {"form":form, 'mensaje':'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'AppMVT/login.html', {"form":form, 'mensaje':'Usuario o contraseña incorrectos'})
    else:
        form=AuthenticationForm()
        return render(request, 'AppMVT/login.html', {'form':form})

def register(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            #podriamos fijarnos que no exista un user en la bd con ese nombre

            form.save()
            return render(request, 'AppMVT/inicio.html', {'mensaje':f"Usuario {username} creado"})
    else:
        form=UserRegisterForm()
    return render(request, 'AppMVT/register.html', {'form':form})



# @login_required        
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form= UserEditForm(request.POST)
        if form.is_valid():
            usuario.first_name=form.cleaned_data["first_name"]
            usuario.last_name=form.cleaned_data["last_name"]
            usuario.email=form.cleaned_data["email"]
            usuario.password1=form.cleaned_data["password1"]
            usuario.password2=form.cleaned_data["password2"]
            usuario.save()
            return render(request, 'AppMVT/inicio.html', {'mensaje':f"Perfil de {usuario} editado"})
    else:
        form= UserEditForm(instance=usuario)
    return render(request, 'AppMVT/editarPerfil.html', {'form':form, 'usuario':usuario})





   


































# def personas(request):
#     personas=Persona.objects.all()
#     print(personas)
#     return render(request, "AppMVT/personas.html", {"personas":personas})

# def entrenadores(request):
#     entrenadores=Entrenador.objects.all()
#     print(entrenadores)
#     return render(request, "AppMVT/entrenadores.html", {"entrenadores":entrenadores})

# def rutas(request):
#     rutas=Ruta.objects.all()
#     print(rutas)
#     return render(request, "AppMVT/rutas.html", {"rutas":rutas})

# def rutaFormulario(request):

#     if request.method=="POST":
#         miFormulario= RutaFormulario(request.POST)
#         print(miFormulario)
#         if miFormulario.is_valid():
#             info=miFormulario.cleaned_data
#             print(info)
#             rutaNueva=Ruta(nombre=info['nombre'],ubicacion=info['ubicacion'],longitud=info['longitud'],vigencia=info['vigencia'])
#             rutaNueva.save()
#             return render(request, "AppMVT/inicio.html")    
#     else:
#         miFormulario=RutaFormulario()
#     return render(request, "AppMVT/rutaFormulario.html", {"miFormulario":miFormulario})

# def personaFormulario(request):

#     if request.method=="POST":
#         miFormulario= PersonaFormulario(request.POST)
#         print(miFormulario)
#         if miFormulario.is_valid():
#             info=miFormulario.cleaned_data
#             print(info)
#             personaNueva=Persona(nombre=info['nombre'],apellido=info['apellido'],edad=info['edad'],
#             ubicacion=info['ubicacion'],email=info['email'])
#             personaNueva.save()
#             return render(request, "AppMVT/inicio.html")    
#     else:
#         miFormulario=PersonaFormulario()
#     return render(request, "AppMVT/personaFormulario.html", {"miFormulario":miFormulario})

# def entrenadorFormulario(request):

#     if request.method=="POST":
#         miFormulario= EntrenadorFormulario(request.POST)
#         print(miFormulario)
#         if miFormulario.is_valid():
#             info=miFormulario.cleaned_data
#             print(info)
#             entrenadorNuevo=Entrenador(nombre=info['nombre'],apellido=info['apellido'],edad=info['edad'],
#             ubicacion=info['ubicacion'],nivel=info['nivel'],email=info['email'])
#             entrenadorNuevo.save()
#             return render(request, "AppMVT/inicio.html")    
#     else:
#         miFormulario=EntrenadorFormulario()
#     return render(request, "AppMVT/entrenadorFormulario.html", {"miFormulario":miFormulario})



# def busquedaRuta (request):
#     return render (request, "AppMVT/busquedaRuta.html")

# def buscar(request):
#     if request.GET ["ubicacion"]:
    
#         ubicacion = request.GET['ubicacion']
#         ubicacionRuta = Ruta.objects.filter(ubicacion=ubicacion)
    
#         return render (request, "AppMVT/busquedaRuta.html",{"rutas":ubicacionRuta, "ubicacion":ubicacion})
    
#     else:
        
#         respuesta = "No enviaste datos"
        
#     return  HttpResponse(respuesta)
