from django.contrib import admin
from apps.paquete_unidad_espacial.models import *

# Register your models here.
admin.site.register(COL_UnidadEspacial)
admin.site.register(CR_Construccion)
admin.site.register(CR_UnidadConstruccion)
admin.site.register(CR_CaracteristicasUnidadConstruccion)
admin.site.register(CR_Terreno)
