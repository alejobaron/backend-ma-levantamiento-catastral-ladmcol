from rest_framework import serializers

from apps.soporte_documental.models import COL_Fuente, COL_FuenteAdministrativa, LC_FuenteAdministrativa, COL_FuenteEspacial, CR_FuenteEspacial

class COL_FuenteSerializer(serializers.ModelSerializer):

    class Meta:
        model = COL_Fuente
        exclude = ('state','created_date', 'modified_date', 'deleted_date')

class COL_FuenteAdministrativaSerializer(serializers.ModelSerializer):

    class Meta:
        model = COL_FuenteAdministrativa
        exclude = ('state','created_date', 'modified_date', 'deleted_date')

class LC_FuenteAdministrativaSerializer(serializers.ModelSerializer):

    class Meta:
        model = LC_FuenteAdministrativa
        exclude = ('state','created_date', 'modified_date', 'deleted_date')

class COL_FuenteEspacialSerializer (serializers.ModelSerializer):

    class Meta:
        model = COL_FuenteEspacial
        exclude = ('state','created_date', 'modified_date', 'deleted_date')

class CR_FuenteEspacialSerializer (serializers.ModelSerializer):

    class Meta:
        model = CR_FuenteEspacial
        exclude = ('state','created_date', 'modified_date', 'deleted_date')
