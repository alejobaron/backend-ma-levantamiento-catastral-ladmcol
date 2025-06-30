from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'

    def ready(self):
        from django.apps import apps  
        Group = apps.get_model('auth', 'Group') 

        group_names = [
            "COORDINADOR CATASTRAL",
            "RECONOCEDOR PREDIAL",
            "PROFESIONAL SIG",
            "JURIDICO",
            "INVITADO",
        ]

        for group_name in group_names:
            Group.objects.get_or_create(name=group_name)

            