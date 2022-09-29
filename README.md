Bienvenidos a nuestro blog de Trekking.

Este es un blog creado por Ramiro Gonzalez y Pablo Buzas.

En la base de datos, esta la informacion correspondiente para que puedan visualizar algunos posts, y probar las funciones como ser "Ver mas" y realizar comentarios a los mismos.

La reparticion de tareas fue la siguiente:

Ramiro: Encagargado de crear el archivo base llamado "padre.html", con su plantilla de Bootstrap correspondiente, y de generar el modelo "Post" junto con los views correspondientes a post, post detalle, register, login y logout.

Pablo: Encargado de generar los avatar para que pueda usar cada usuario, y hacer que quede de un tamaño y posicion coherente, junto con el modelo para realizar comentarios en los post, y hacer ajustes esteticos en general.

-------------------------------------------------------------

Pasos para ejecutar el repositorio:

Instrucciones:
-   Instalar Python desde la web oficial

-   Clonar el proyecto

-   Instalar las dependencias del proyecto:

    Automaticamente:

    pip install -r requirements.txt
    De forma manual:

    pip install django
    pip install Pillow

-   Realizar las migraciones para generar la base de datos

    python manage.py makemigrations
    python manage.py migrate
    Correr la aplicacion

    python manage.py runserver

Habiendo realizado correctamente los pasos, ya podras ingresar al Blog, a traves de:

http://127.0.0.1:8000/
