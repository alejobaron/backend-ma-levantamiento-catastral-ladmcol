from rest_framework import serializers

from apps.estructuras.models import ExtDireccion, ExtInteresado, LC_EstructuraNovedadNumeroPredial, LC_NovedadFMI, ExtArchivo, COL_AreaValor, COL_VolumenValor

class ExtDireccionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExtDireccion
        exclude = ('state','created_date','modified_date','deleted_date')

class ExtinteresadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExtInteresado
        exclude = ('state','created_date','modified_date','deleted_date')
        
class EstructuraNovedadNumeroPredialSerializer(serializers.ModelSerializer):
    numero_predial = serializers.CharField(
        min_length=30,
        max_length=30,
        required=True,
        help_text='Debe contener exactamente 30 dígitos.'
    )
    
    class Meta:
        model = LC_EstructuraNovedadNumeroPredial
        exclude = ('state','created_date','modified_date','deleted_date')
    
class NovedadFMISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LC_NovedadFMI
        exclude = ('state','created_date','modified_date','deleted_date')
        
class ExtArchivoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExtArchivo
        exclude = ('state','created_date','modified_date','deleted_date')
        
class AreaValorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = COL_AreaValor
        exclude = ('state','created_date','modified_date','deleted_date')
        
class VolumenValorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = COL_VolumenValor
        exclude = ('state','created_date','modified_date','deleted_date')
        
