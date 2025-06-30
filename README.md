# Plataforma Digital para la Gestión Catastral en Colombia: Implementación del modelo de aplicación de levantamiento catastral LADM COL

Este proyecto tiene como finalidad presentar el desarrollo e implementación de una plataforma digital orientada a la gestión catastral en Colombia, tomando como base normativa y técnica el Modelo de Aplicación de Levantamiento Catastral LADM-COL en su versión 2.0.

El backend de la plataforma se construye con Django REST Framework (DRF) y extensiones geoespaciales mediante GeoDjango y PostGIS, permitiendo exponer servicios web robustos y seguros y donde se explica su estructura en este archivoc.

---

## Estructura del Proyecto

El proyecto está organizado en aplicaciones creadas mediante sentencias de codigo de DRF, cada una representa diferentes componentes temáticos del modelo de aplicación del levantamiento catastral LADM-COL, trabajando unicamente los paquetes adiministrativos, interesados, unidad espacial y el componente de soporte documental

| Aplicación               | Descripción                                                                					  |
|--------------------------|--------------------------------------------------------------------------------------------------|
| 'dominios'               | Contiene entidades de dominio y catálogos de clasificación.                					  |
| 'estructuras'            | Define estructuras adicionales y asociativas de algunas entidades del modelo.                    |
| 'paquete_administrativo' | Modela la información administrativa (derechos, restricciones, etc.).      					  |
| 'paquete_interesados'    | Representa personas naturales o jurídicas involucradas.                    					  |
| 'paquete_unidad_espacial'| Contiene las unidades espaciales como predios o parcelas.                  					  |
| 'soporte_documental'     | Administra documentos que respaldan la información catastral.              					  |
| 'users'                  | Gestión de usuarios y autenticación.                                       					  |

---

## Arquitectura de cada aplicación

Cada aplicación cuenta con la siguiente estructura interna:

<pre> nombre_aplicacion/ 
 │
 ├── models.py # Definición de entidades del modelo LADM-COL 
 ├── admin.py # Registro de modelos en el panel de administración 
 ├── apps.py # Configuración de la app 
 │ 
 └── api/ 
 ├── serializers.py # Serialización de modelos (ModelSerializer) 
 ├── views.py # Vistas basadas en ViewSets (ModelViewSet) 
 └── routers.py # Registro de rutas por modelo (router.register) </pre>

---

## Configuración del Proyecto

El proyecto principal que lleva de nombre 'MA_LEVANTAMIENTO_CATASTRAL' contiene:
<pre>
settings.py # Configuración general de Django, DRF, CORS, BD, etc.
urls.py # Enrutamiento global de APIs.
Integración con PostgreSQL.</pre>

---

## Tecnologías Utilizadas

- Python 3.12.3
- Django 5.1.1
- Django REST Framework 3.15.2
- PostgreSQL 

---


## Instalación y Uso

- Clonar el repositorio

- Crear entorno virtual e instalar dependencias
```bash
python -m venv env
source bin/activate
pip install -r requirements.txt
```

- Creación de base de datos en PostgreSQL con extension PostGIS  configuración del sistema de referencia MAGNA-SIRGAS Origen Nacional
 
- Configurar la base de datos (PostgreSQL)
Editar el archivo settings.py con las credenciales PostgreSQL:
<pre> DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'nombre_bd',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
} </pre>

- Migraciones y superusuario
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

- Ejecutar el servidor
```bash
python manage.py runserver
```

- Una vez el servidor esté en funcionamiento, puedes acceder a los endpoints en:
http://localhost:8000/api/

- En la interfaz de administración de Django en:
http://localhost:8000/admin/

