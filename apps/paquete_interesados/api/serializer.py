from rest_framework import serializers

from apps.paquete_interesados.models import COL_Interesado, CR_Interesado, COL_AgrupacionInteresados, col_miembros, CR_AgrupacionInteresados, LC_InteresadoContacto

class COL_InteresadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = COL_Interesado
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class CR_InteresadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CR_Interesado
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class COL_AgrupacionInteresadosSerializer(serializers.ModelSerializer):

    class Meta:
        model = COL_AgrupacionInteresados
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class col_miembrosSerializer(serializers.ModelSerializer):

    class Meta:
        model = col_miembros
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class CR_AgrupacionInteresadosSerializer(serializers.ModelSerializer):

    class Meta:
        model = CR_AgrupacionInteresados
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class LC_InteresadoContactoSerializer(serializers.ModelSerializer):

    class Meta:
        model = LC_InteresadoContacto
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
