from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RutaFormulario(forms.Form):
    #especificar los campos
    nombre=forms.CharField(max_length=50)
    ubicacion=forms.CharField(max_length=50)
    longitud=forms.IntegerField()
    vigencia=forms.IntegerField()
