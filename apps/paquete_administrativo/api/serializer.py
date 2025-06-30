from rest_framework import serializers

from apps.paquete_administrativo.models import COL_UnidadAdministrativaBasica, LC_Predio, cr_predio_copropiedad, CR_DatosPHCondominio, LC_DatosAdicionalesLevantamientoCatastral, LC_ContactoVisita, COL_DRR, LC_Derecho

class COL_UnidadAdministrativaBasicaSerializer(serializers.ModelSerializer):
    """ tipo_UAB_nombre = serializers.CharField(source='tipo_UAB.tipo', read_only=True) """
    tipo_UAB_nombre = serializers.SerializerMethodField()

    class Meta:
        model = COL_UnidadAdministrativaBasica
        exclude = ('state','created_date','modified_date','deleted_date')
        
    def get_tipo_UAB_nombre(self, obj):
        if obj.tipo_UAB and obj.tipo_UAB.tipo:
            return obj.tipo_UAB.tipo.replace('_', ' ').title()
        return ""

class LC_PredioSerializer(serializers.ModelSerializer):
    nombre_UAB = serializers.SerializerMethodField()

    class Meta:
        model = LC_Predio
        exclude = ('state','created_date','modified_date','deleted_date')
        
    def get_nombre_UAB(self, obj):
        if obj.unidad_basica_administrativa and obj.unidad_basica_administrativa.nombre:
            return obj.unidad_basica_administrativa.nombre
        return ""

class cr_predio_copropiedadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = cr_predio_copropiedad
        exclude = ('state','created_date','modified_date','deleted_date')

class CR_DatosPHCondominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CR_DatosPHCondominio
        exclude = ('state','created_date','modified_date','deleted_date')

class LC_DatosAdicionalesLevantamientoCatastralSerializer(serializers.ModelSerializer):

    class Meta:
        model = LC_DatosAdicionalesLevantamientoCatastral
        exclude = ('state','created_date','modified_date','deleted_date')

class LC_ContactoVisitaSerializer(serializers.ModelSerializer):

    class Meta:
        model = LC_ContactoVisita
        exclude = ('state','created_date','modified_date','deleted_date')

class COL_DRRSerializer(serializers.ModelSerializer):

    class Meta:
        model = COL_DRR
        exclude = ('state','created_date','modified_date','deleted_date')

class LC_DerechoSerializer(serializers.ModelSerializer):

    class Meta:
        model = LC_Derecho
        exclude = ('state','created_date','modified_date','deleted_date')
