from django.db import models


# Create your models here.
    
class Padre(models.Model):
    
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=40)
    
class Madre(models.Model):
    
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=40)
        
class Novia(models.Model):
    
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=40)
    

