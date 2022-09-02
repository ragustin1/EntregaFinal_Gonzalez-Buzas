from django.urls import path
from .views import *


urlpatterns = [
      path('personas/', personas, name='personas'),
    path('entrenadores/', entrenadores, name='entrenadores'),
    path('rutas/', rutas, name='rutas'),
    path('rutaFormulario/', rutaFormulario, name='rutaFormulario'),
    path('', inicio, name='inicio'),
    path('busquedaRuta/', busquedaRuta, name='busquedaRuta'),
    path('buscar/', buscar),
    ]