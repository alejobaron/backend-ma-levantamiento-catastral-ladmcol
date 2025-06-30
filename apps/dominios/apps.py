from django.apps import AppConfig


class DominiosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.dominios'
    
    def ready(self):
        from .models import cargar_datos_iniciales
        cargar_datos_iniciales()
    
    

