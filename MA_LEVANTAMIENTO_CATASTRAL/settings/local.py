from .base import*

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'modelo_levantamiento_v2',
        'USER': 'abaron2024',
        'PASSWORD': 'proyecto2024',
        'HOST': 'localhost',
        'PORT': '5432',  # Puerto predeterminado de PostgreSQL
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'