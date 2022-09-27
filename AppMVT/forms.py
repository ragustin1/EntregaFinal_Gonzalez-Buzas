from xml.etree.ElementTree import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment


class RutaFormulario(forms.Form):
    #especificar los campos
    nombre=forms.CharField(max_length=50)
    ubicacion=forms.CharField(max_length=50)
    longitud=forms.IntegerField()
    vigencia=forms.IntegerField()
    
class PersonaFormulario(forms.Form):
    #especificar los campos
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    ubicacion=forms.CharField(max_length=50)
    email=forms.EmailField()
    
class EntrenadorFormulario(forms.Form):
    #especificar los campos
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    ubicacion=forms.CharField(max_length=50)
    nivel=forms.CharField(max_length=50)
    email=forms.EmailField()

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email=forms.EmailField(label='Modificar E-Mail')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['nombre', 'correo', 'body']