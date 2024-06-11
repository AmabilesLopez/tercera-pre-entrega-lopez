PROYECTO FIBRA OPTICA

"Este proyecto de Django gestiona la instalación de servicios de fibra óptica. A continuación se describe la estructura del proyecto, la funcionalidad de cada módulo y el orden en que se deben probar las características".

Estructura del Proyecto:

fibra_optica/
    __pycache__/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
servicios/
    __pycache__/
    __init__.py
    admin.py
    apps.py
    forms.py
    models.py
    urls.py
    views.py
    migrations/
        __pycache__/
        __init__.py
        0001_initial.py
templates/
    servicios/
        base.html
        detalle_instalacion.html
        home.html
        lista_instalaciones.html
        registrar_cliente.html
        registrar_instalacion.html
db.sqlite3
manage.py

Funcionalidades Principales:

Página de Inicio

Ruta: /
Archivo: servicios/views.py (función home)
Plantilla: templates/servicios/home.html
Descripción: Página principal del servicio de instalación de fibra óptica.
Registrar Cliente

Ruta: /registrar_cliente/
Archivo: servicios/views.py (función registrar_cliente)
Plantilla: templates/servicios/registrar_cliente.html
Descripción: Formulario para registrar un nuevo cliente.
Registrar Instalación

Ruta: /registrar_instalacion/
Archivo: servicios/views.py (función registrar_instalacion)
Plantilla: templates/servicios/registrar_instalacion.html
Descripción: Formulario para registrar una nueva instalación de fibra óptica.
Lista de Instalaciones

Ruta: /lista_instalaciones/
Archivo: servicios/views.py (función lista_instalaciones)
Plantilla: templates/servicios/lista_instalaciones.html
Descripción: Muestra una lista de todas las instalaciones registradas.
Detalle de Instalación

Ruta: /instalacion/<int:pk>/
Archivo: servicios/views.py (función detalle_instalacion)
Plantilla: templates/servicios/detalle_instalacion.html
Descripción: Muestra el detalle de una instalación específica.
Modelos
Cliente

Archivo: servicios/models.py
Descripción: Representa a un cliente del servicio de fibra óptica.
Campos: nombre, apellido, direccion, telefono, correo
Instalacion

Archivo: servicios/models.py
Descripción: Representa una instalación de fibra óptica.
Campos: cliente, tipo_fibra, router_bicanal, extensor_wifi, fecha_instalacion, hora_instalacion, comentario_adicional
Formularios
ClienteForm

Archivo: servicios/forms.py
Descripción: Formulario para crear un cliente.
Modelo: Cliente
Campos: nombre, apellido, direccion, telefono, correo
InstalacionForm

Archivo: servicios/forms.py
Descripción: Formulario para crear una instalación.
Modelo: Instalacion
Campos: cliente, tipo_fibra, router_bicanal, extensor_wifi, fecha_instalacion, hora_instalacion, comentario_adicional
Pruebas


Orden de Pruebas:
Configurar y Ejecutar el Proyecto:

***Ejecutar migraciones: python manage.py migrate***
Iniciar el servidor de desarrollo: python manage.py runserver
Página de Inicio

Visitar: http://127.0.0.1:8000/
Verificar que se muestra la página de inicio correctamente.
Registrar Cliente

Visitar: http://127.0.0.1:8000/registrar_cliente/
Completar el formulario y enviar.
Verificar que se redirige a la página de inicio y que el cliente se ha guardado en la base de datos.
Registrar Instalación

Visitar: http://127.0.0.1:8000/registrar_instalacion/
Completar el formulario y enviar.
Verificar que se redirige a la página de inicio y que la instalación se ha guardado en la base de datos.
Lista de Instalaciones

Visitar: http://127.0.0.1:8000/lista_instalaciones/
Verificar que se muestra la lista de todas las instalaciones.
Detalle de Instalación

Desde la lista de instalaciones, hacer clic en una instalación para ver su detalle.
Verificar que se muestra correctamente toda la información de la instalación seleccionada.

***Notas***:
Migraciones: Las migraciones se encuentran en el directorio servicios/migrations/.
Plantillas: Las plantillas HTML se encuentran en el directorio templates/servicios/.
Para el acceso de administrador http://127.0.0.1:8000/admin/ se creó el superuser: amabiles y la contraseña:123456789

Ejecución del Proyecto:

1. Crear y activar un entorno virtual:
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

2. Instalar las dependencias
pip install -r requirements.txt

3. Ejecutar migraciones
python manage.py migrate

4. iniciar el servidor
python manage.py runserver

5. Visitar http://127.0.0.1:8000/ en el navegador.

¡Disfruta usando tu aplicación de gestión de instalaciones de fibra óptica!
