# Platzigram | Django App

## 1. Configuración del entorno

Para instalar nuestro entorno virtual usando conda podemos ejecutar:

```bash
conda create --name platzigram 
```

Para instalar Django hacemos:

```bash
conda install django
```

Por último debemos generar un archivo yaml con la configuración de nuestro venv, para ello ejecutamos en la terminal:

```bash
conda env export > paltzigram.yml 
```

## 2. Primeros pasos

Django tiene una interfaz de linea de comandos que podemos abrir con **django-admin** que nos muestra otras opciones que podemos usar en Django para trabajar con nuestro proyecto. Al usarlo el resultado es algo parecido a esto:

```bash
Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
```

A través del uso de esta interfaz podemos crear nuestro proyecto de django con tan solo usar:

```bash
django-admin startproject <nombre del proyecto> <ubicacion_del_proyecto>
```

por ejemplo: 

```bash
django-admin startproject platzigram .
```

Los archivos que nos genera Django con esto son: 

- **\_init\_** Declara nuestro proyecto como un modulo de python.
- **settings** Define todas las configuraciones de nuestro proyecto.
- **urls** El punto de entrada para todas las peticiones que lleguen a nuestro proyecto de Django. Tratara de buscar la url requerida y asociarla con su vista correspondiente. 
- **wsgi** Archivo usado para producción.
- **manage** Archivo auto generado con el que interactuaremos durante todo el desarrollo.


### Archivo de settings

En el archivo de settings podremos configurar diferentes cosas de nuestro proyecto como:

- BASE_DIR: El directorio de nuestra aplicación.
- SECRET_KEY: La clave con la cual se harán todos los hashes en nuestro proyecto.
- DEBUG: Variable que controla el modo de desarrollo o producción

- ALLOWED_HOSTS: Array que contiene los hosts autorizados para solicitar requests (Politicas de CORS).

También podremos configurar aplicaciones para volver mas robusto nuestro proyecto. Django por defecto cuenta con los siguientes módulos de aplicación instalados.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
También podemos instalar middlewares que interceptaran nuestros requests para agregarles funcionalidades o validaciones extras. Por defecto los siguientes Middlewares vienen instalados en los proyectos de Django.

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Otras de las configuraciones que podemos aplicar en este archivo son:

- Definición de nuestro archivo de urls
- Configuración de templates
- Manejo de archivo a producción (WSGI)
- Definición del motor de la base de datos
- Validadores de contraseñas
- Lenguaje con el que se interactúa
- Timezone
- Opciones para traducción
- Resolución de archivos estáticos

### Levantar el servidor

```bash
python manage.py runserver
```

**Output**

```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

February 01, 2020 - 02:04:54
Django version 2.2.5, using settings 'platzigram.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[01/Feb/2020 02:04:59] "GET / HTTP/1.1" 200 16387
```
## 3. Creando vistas

Django es una interfaz para poder madar requests a traves de urls, para ello usa vistas que presentan la informacion que desea mandar al cliente. Esto se define en el archivo de urls de la siguiente manera:

```python
from django.urls import path # Modulo de URLS

# Modulo de HTTP, nos permite manejar la respuesta del request.
from django.http import HttpResponse 

# Definicion de la vista a traves de una funcion, esta maneja como
# parametro el request para que django lo encuentre

def hello_world(reques):
    return HttpResponse('Hello world') # Mandamos "Hello world" al cliente


urlpatterns = [
    path('hello-world/', hello_world),
]

```

Al tratarse de python podemos dividir nuestro código en módulos por lo que podemos crear un archivo especifico para las vistas.

```python
from django.http import HttpResponse

def hello_world(reques):
    return HttpResponse('Hello world')
```

Al final solo debemos importar este modulo a nuestro archivo de urls y asignar la vista que queremos.

```python
from django.urls import path
from platzigram import views

urlpatterns = [
    path('hello-world/', views.hello_world),
]
```

Podemos ir agregando mas vistas y añadirlas a nuestras rutas en el archivo de urls.

```python
#Vista
def see_date_time(request):
    now = datetime.now().strftime('%dth %b, %Y - %H:%Mhrs')
    return HttpResponse(f'Oh! La fecha de hoy es {str(now)}')
```

```python
# Definicion en el archivo de urls
urlpatterns = [
    path('hello-world/', views.hello_world),
    path('date-time/', views.see_date_time),
]
```

### Path Converters

Nos ayudan a pasar parámetros a nuestras vistas, se declaran de la siguiente forma:

```python
urlpatterns = [
    path('access/<str:name>/<int:age>', views.get_access_by_age),
]
```

Para poder usarlos en nuestras vistas solo es necesario pasarlos como un argumento en nuestra función de vista.


```python
def get_access_by_age(request, name, age):
    message = ''
    if age >= 18:
        message = f'Bienvenido de nuevo {name}!'
    else:
        message = f'Acceso no permitido a menores de 18, lo lamentamos {name}'

    return HttpResponse(message)
```
## 4. Creación de App con Django

Para crear una app solo debemos ejecutar:

```bash
python manage.py startapp <nombre_de_la_app>
```

y al final solo debemos agregarla a nuestra configuración principal de nuestro proyecto

```python
INSTALLED_APPS = [
    #Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Local Apps
    '<nombre_de_la_app>',
]
```
## 5. MTV (Model-Template-View)

> Un patrón de diseño, en términos generales, es una solución reutilizable a un problema común. 

El patrón más común para el desarrollo web es MVC (Model, View, Controller). Django implementa un patrón similar llamado MTV (Model, Template, View).

![MTV](https://www.dropbox.com/s/uw1doivshzalc3i/MTV.png?raw=1)

### Model

> Es la forma en la que creamos esquemas de objetos (un usuario, un post, etc) para representarlos en nuestra base de datos. 

El modelo sin importar nuestro sistema ge BD (mysql, postgress, etc) nos ayudara a crear esta entidad a través de un OMR, esto nos ahorra la molestia de tener que escribir las sentencias de SQL para crear las tablas y atributos. 

### Template

Es el encargado de manejar la lógica y sintaxis de la información que se va a presentar en el cliente, el sistema de templates de django usa HTML para ello.

### View

> *Su función es solo suministrar datos al template*

Manda la información necesaria el template para que este pueda manejar los datos y presentarlos de una manera correcta. 


## 6. Migraciones

Las migraciones son la manera en la cual podemos propagar los cambios en nuestros modelos a la base de datos, esto nos ahorra la necesidad de hacer cambios directamente en nuestro gestor de base de datos. Para ello ejecutamos:

```bash
python manage.py migrate
```

Por defecto Django usa **sqlite** como sistema de DB, sin embargo podemos usar diferentes gestores, en la [documentacion](https://docs.djangoproject.com/en/2.2/ref/settings/#databases) oficial de Django se especifica mas al respecto.

## 7. Creación de un modelo

```python
#Modelando la entidad de usuario
from django.db import models


class User(models.model):

    email =  models.EmailField()
    password = models.CharField()

    fist_name = models.CharField()
    bio = models.TextField()

    birthdate = models.DateField()

    created = models.DateTimeField()
    updated = models.DateTimeField()
```

Existen diferentes campos que se pueden usar en los modelos, se puede consultar en el [siguiente](https://docs.djangoproject.com/en/3.0/ref/models/fields/) enlace para saber mas sobre ellos.

Dependiendo del tipo de campo que usemos podremos agregarle restricciones o filtros para definir su comportamiento; por ejemplo, un usuario puede que su nombre no deba ser mayor a 100 caracteres, o que su fecha de nacimiento no sea requerida como campo obligatorio.

```python
# Django
from django.db import models


class User(models.Model):

    email = models.EmailField()
    password = models.CharField(max_length=100)

    fist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
```

Para reflejar esos cambios de nuestro modelos en la base de datos ejecutamos:

```bash
python manage.py makemigrations
```

Al realizar las migraciones se creara una carpeta llamada *migrations* en la cual se especifica las migraciones que se han hecho y especifica en archivo auto generados por Django que fue lo que se hizo, como agregar o modificar un modelo.

```python
# Generated by Django 2.2.5 on 2020-02-03 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('fist_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('birthdate', models.DateField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

```

Para aplicar esta migración corremos:

```bash
python manage.py migrate
```