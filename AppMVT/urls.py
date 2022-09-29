from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [    
    path('', inicio, name='inicio'),   
    path('about/', about, name='about'),
    path('sample/', sample, name='sample'),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='AppMVT/logout.html'), name='logout'),
    path('<slug:slug>/', postDetalle, name = 'postDetalle'),
    path('editarPerfil', editarPerfil, name = 'editarPerfil')
    ]



    
    # path('personas/', personas, name='personas'),
    # path('entrenadores/', entrenadores, name='entrenadores'),
    # path('rutas/', rutas, name='rutas'),
    # path('rutaFormulario/', rutaFormulario, name='rutaFormulario'),
    # path('personaFormulario/', personaFormulario, name='personaFormulario'),
    # path('entrenadorFormulario/', entrenadorFormulario, name='entrenadorFormulario'),
    # path('busquedaRuta/', busquedaRuta, name='busquedaRuta'),
    # path('buscar/', buscar),  