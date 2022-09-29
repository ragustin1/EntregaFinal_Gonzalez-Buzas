from django.contrib import admin

from AppMVT.models import Post, Avatar

# Register your models here.

# Importamos el modelo POST y lo registramos en la linea 12

admin.site.register(Post)
admin.site.register(Avatar)