from rest_framework import serializers
from apps.dominios.models import COL_UnidadAdministrativaBasicaTipo, LC_PredioTipo, LC_CondicionPredioTipo, LC_DestinacionEconomicaTipo, LC_ResultadoVisitaTipo, CR_DocumentoTipo, LC_DerechoTipo, CR_InteresadoTipo, CR_SexoTipo, CR_GrupoEtnicoTipo, COL_GrupoInteresadoTipo, COL_EstadoDisponibilidadTipo, CI_Forma_Presentacion_Codigo, COL_FuenteAdministrativaTipo, LC_FuenteAdministrativaTipo, COL_FuenteEspacialTipo, COL_DimensionTipo, COL_RelacionSuperficieTipo, CR_UnidadConstruccionTipo, CR_UsoUConsTipo, CR_ConstruccionPlantaTipo

class COL_UnidadAdministrativaBasicaTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = COL_UnidadAdministrativaBasicaTipo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class LC_PredioTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = LC_PredioTipo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class LC_CondicionPredioTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = LC_CondicionPredioTipo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class LC_DestinacionEconomicaTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = LC_DestinacionEconomicaTipo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class LC_ResultadoVisitaTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_resultado_display', read_only=True)

    class Meta:
        model = LC_ResultadoVisitaTipo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class CR_DocumentoTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = CR_DocumentoTipo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class LC_DerechoTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = LC_DerechoTipo
        exclude = ('state','created_date','modified_date','deleted_date')

class CR_InteresadoTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = CR_InteresadoTipo
        exclude = ('state','created_date','modified_date','deleted_date')
        
        
class CR_SexoTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = CR_SexoTipo
        exclude = ('state','created_date','modified_date','deleted_date')

class CR_GrupoEtnicoTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = CR_GrupoEtnicoTipo
        exclude = ('state','created_date','modified_date','deleted_date')

class COL_GrupoInteresadoTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = COL_GrupoInteresadoTipo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class COL_EstadoDisponibilidadTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = COL_EstadoDisponibilidadTipo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class CI_Forma_Presentacion_CodigoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_codigo_display', read_only=True)

    class Meta:
        model = CI_Forma_Presentacion_Codigo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class COL_FuenteAdministrativaTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = COL_FuenteAdministrativaTipo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class LC_FuenteAdministrativaTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = LC_FuenteAdministrativaTipo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class COL_FuenteEspacialTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = COL_FuenteEspacialTipo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class COL_DimensionTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = COL_DimensionTipo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class COL_RelacionSuperficieTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = COL_RelacionSuperficieTipo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class CR_UnidadConstruccionTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = CR_UnidadConstruccionTipo
        exclude = ('state','created_date','modified_date','deleted_date')

class CR_UsoUConsTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = CR_UsoUConsTipo
        exclude = ('state','created_date','modified_date','deleted_date') 
        
class CR_ConstruccionPlantaTipoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = CR_ConstruccionPlantaTipo
        exclude = ('state','created_date','modified_date','deleted_date')      
        

        
        

        
        
        
        
        
        
    
        
        
        
        
        
        
        
        


