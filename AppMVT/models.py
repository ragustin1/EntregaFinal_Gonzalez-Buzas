from django.db import models

# Create your models here.


class Ruta(models.Model):
    nombre=models.CharField(max_length=50)
    ubicacion=models.CharField(max_length=50)
    longitud=models.IntegerField()
    vigencia=models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre+" en "+self.ubicacion
    
class Persona(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad=models.IntegerField()
    ubicacion=models.CharField(max_length=50)
    email= models.EmailField()
    
    def __str__(self) -> str:
        return self.apellido+" "+self.nombre


class Entrenador(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    ubicacion=models.CharField(max_length=50)
    nivel=models.CharField(max_length=50)
    email=models.EmailField()
    

    def __str__(self) -> str:
        return self.apellido+" "+self.nombre

