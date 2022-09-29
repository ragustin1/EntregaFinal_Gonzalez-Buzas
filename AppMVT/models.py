from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


# class Ruta(models.Model):
#     nombre=models.CharField(max_length=50)
#     ubicacion=models.CharField(max_length=50)
#     longitud=models.IntegerField()
#     vigencia=models.IntegerField()
    
#     def __str__(self) -> str:
#         return self.nombre+" en "+self.ubicacion
    
# class Persona(models.Model):
#     nombre= models.CharField(max_length=50)
#     apellido= models.CharField(max_length=50)
#     edad=models.IntegerField()
#     ubicacion=models.CharField(max_length=50)
#     email= models.EmailField()
    
#     def __str__(self) -> str:
#         return self.apellido+" "+self.nombre


# class Entrenador(models.Model):
#     nombre=models.CharField(max_length=50)
#     apellido=models.CharField(max_length=50)
#     edad=models.IntegerField()
#     ubicacion=models.CharField(max_length=50)
#     nivel=models.CharField(max_length=50)
#     email=models.EmailField()
    

#     def __str__(self) -> str:
#         return self.apellido+" "+self.nombre

# Creamos la clase Post. Ver que es el SLUG y si podemos renombrarlo.
# Tambien creamos la variable fechaCreacion, para que se pueda asignar la fecha cuando fue creado el posteo.
class Post(models.Model):
    title = models.CharField (max_length=255)
    slug = models.SlugField()
    intro = models.TextField() 
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    imagenCabecera = models.ImageField(null = True, blank = True, upload_to = "images/")
    #autor = models.TextField()
    
    class Meta:
        ordering = ['-fechaCreacion'] # Aca el nombre debe coincidir con el modelo creado para las fechas de creacion.
    
    # def __str__(self):
    #     return f"Titulo: {self.title} - Introduccion: {self.intro} - Cuerpo: {self.body} - Creado: {self.fechaCreacion} "
# Lo mande a comentario, para quitarle info, y mostrar solo lo que creemos mas relevante.

    def __str__(self):
        return f"Titulo: {self.title} - Creado: {self.fechaCreacion} "
    
# class Avatar(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     imagen = models.ImageField(upload_to='avatares', null = True, blank = True)
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = 'comments', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    body = models.TextField()
    fechaComentario = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-fechaComentario']
        

