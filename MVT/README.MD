Esto es una continuacion del trabajo anterior, con algunas modificaciones!

Venimos a presentar nuestra pagina de trekking!

Retomando desde la entrega inicial, se trabajo optimizando los archivos, para disminuir las lineas de codigo y hacer mas entendible cada una de ellas.

Como mejora, se utilizo el metodo "render", en lugar del "HttpResponse", haciendo el codigo mas amigable.
Por otro lado, se implemento un modelo de Bootstrap, para hacer mas amigable el entorno visual, y se configuraron algunas de sus funcionalidades, quedando pendiente varias modificaciones. 

A grandes rasgos se fueron migrando los archivos a la App llamada "AppMVT", para lograr una implementacion mas limpia y simplificada.

En esta pagina van a poder Registrar sus rutas de Trekking, como asi tambien realizar busquedas de rutas existentes, ingresando la ubicacion geografica que deseen. Para esto fue necesario trabajar con la base de datos y crear un superusuario, para poder acceder al modo admin, y agregar/modificar/eliminar datos.

---------------------------------------------------------------------------------------------------------------

A continuacion el tutorial de como utilizar nuestra pagina:

- En el inicio, el cual es "/AppMVT", podran ver el contenido general de la pagina, desde alli podran acceder a traves de los botones, a las siguientes opciones:

- "Registra tu ruta!", la cual te lleva a la url "/AppMVT/rutaFormulario/", donde podras registrar tu ruta de trekking, para ello deberas darle el nombre que quieras a esa ruta, poner su ubicacion, su ubicacion geografica como mas prefieras, y por ultimo en vigencia, deberas colocar desde cuando existe esa ruta.

- "Encontra tu ruta!", te lleva a "/AppMVT/busquedaRuta/" donde te permite buscar una ruta en la base de datos, ingresando solamente la ubicacion de tu preferencia.

- "Rutas" te direcciona a "/AppMVT/rutas/" y te permite ver todas las rutas subidas por los usuarios. 

- "Personas" te direcciona a "/AppMVT/personas/" y te permite ver todas los usuarios registrados en la pagina.

- "Entrenadores" te direcciona a "/AppMVT/entrenadores/" y te permite ver todas las entrenadores disponibles que se encuentran registrados.  

---------------------------------------------------------------------------------------------------------------


Espero la pagina sea de su agrado!


