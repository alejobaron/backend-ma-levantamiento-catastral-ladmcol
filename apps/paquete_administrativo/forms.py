from django import forms
from apps.paquete_administrativo.models import LC_Predio
from apps.estructuras.models import ExtDireccion

class LC_PredioForm(forms.ModelForm):
    """LC_PredioForm definition."""

    # TODO: Define form fields here
    direccion = forms.ModelChoiceField(
        queryset=ExtDireccion.objects.all(), 
        required=False, 
        empty_label="Crear dirección", 
        widget=forms.Select(attrs={'class':'form-control'})
    )

    class Meta:
        model = LC_Predio
        fields = '__all__'

