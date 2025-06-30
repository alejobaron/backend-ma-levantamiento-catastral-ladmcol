from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from apps.paquete_unidad_espacial.models import COL_UnidadEspacial, CR_Construccion, CR_CaracteristicasUnidadConstruccion, CR_UnidadConstruccion, CR_Terreno

class COL_UnidadEspacialSerializer(serializers.ModelSerializer):
    class Meta:
        model = COL_UnidadEspacial
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class CR_ConstruccionSerializer(GeoFeatureModelSerializer):
    
    def validate_construccion_geometria(self, value):
        # Validar intersección con otras construcciones
        construcciones = CR_Construccion.objects.exclude(id=self.instance.id if self.instance else None)
        for construccion in construcciones:
            if value.intersects(construccion.construccion_geometria) and not value.touches(construccion.construccion_geometria):
                raise serializers.ValidationError("La geometría se superpone con otra construcción existente.")
        
        # Validar que esté completamente dentro de un solo terreno
        terrenos = CR_Terreno.objects.all()
        terrenos_contiene = [terreno for terreno in terrenos if value.within(terreno.terreno_geometria)]
        
        if not terrenos_contiene:
            raise serializers.ValidationError("La construcción debe estar completamente contenida en un terreno.")
        if len(terrenos_contiene) > 1:
            raise serializers.ValidationError("La construcción está contenida en más de un terreno. Solo debe estar en uno.")
        
        return value

    class Meta:
        model = CR_Construccion
        geo_field = "construccion_geometria"
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class CR_CaracteristicasUnidadConstruccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CR_CaracteristicasUnidadConstruccion
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class CR_UnidadConstruccionSerializer(GeoFeatureModelSerializer):
    
    def validate_unidadconstruccion_geometria(self, value):      
        construcciones = CR_Construccion.objects.all()
        construcciones_contiene = [construccion for construccion in construcciones if value.within(construccion.construccion_geometria)]
        
        if not construcciones_contiene:
            raise serializers.ValidationError("La unidad de construcción debe estar completamente contenida en una construcción.")
        if len(construcciones_contiene) > 1:
            raise serializers.ValidationError("La unidad de construcción está contenida en más de una construcción. Solo debe estar en una.")
        
        return value
    
    def validate_unidad_construccion_geometria(self, value):
        construcciones = CR_Construccion.objects.filter(construccion_geometria__isnull=False)
        construcciones_validas = [construccion for construccion in construcciones
            if value.within(construccion.construccion_geometria)
        ]

        if not construcciones_validas:
            raise serializers.ValidationError(
                "La unidad de construcción debe estar completamente contenida dentro de una construcción.")

        if len(construcciones_validas) > 1:
            raise serializers.ValidationError(
                "La unidad de construcción se encuentra contenida en más de una construcción. Debe estar solo en una.")

        return value


    class Meta:
        model = CR_UnidadConstruccion
        geo_field = "unidad_construccion_geometria"
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class CR_TerrenoSerializer(GeoFeatureModelSerializer):
    
    def validate_terreno_geometria(self, value):
        if value.srid != 9377:
            value.transform(9377)
        terrenos_existentes = CR_Terreno.objects.exclude(id=self.instance.id if self.instance else None)

        for terreno in terrenos_existentes:
            if value.intersects(terreno.terreno_geometria) and not value.touches(terreno.terreno_geometria):
                raise serializers.ValidationError("La geometría del terreno se superpone con otro terreno existente.")
        return value
    
    class Meta:
        model = CR_Terreno
        geo_field = "terreno_geometria"
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
        
        