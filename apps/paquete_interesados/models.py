from django.db import models
from django.core.exceptions import ValidationError
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
from apps.estructuras.models import ExtInteresado
from apps.dominios.models import CR_InteresadoTipo, CR_DocumentoTipo, CR_SexoTipo, CR_GrupoEtnicoTipo, COL_GrupoInteresadoTipo

# Create your models here.
class COL_Interesado(BaseModel):
    """Model definition for COL_Interesado."""

    # TODO: Define fields here
    ext_PID = models.OneToOneField(ExtInteresado, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Identificador del interesado', related_name='interesado_col', help_text='Identificador del interesado.')
    nombre = models.CharField('Nombre', max_length=200, blank=True, null=True, help_text='Nombre del Interesado.')

    class Meta:
        """Meta definition for COL_Interesado."""

        verbose_name = 'Interesado (COL)'
        verbose_name_plural = 'Interesados (COL)'

    def __str__(self):
        """Unicode representation of COL_Interesado."""
        return self.nombre
    
class CR_Interesado(BaseModel):
    """Model definition for CR_Interesado."""

    # TODO: Define fields here
    interesado = models.OneToOneField(COL_Interesado, on_delete=models.CASCADE, verbose_name='ID Interesado', related_name='Interesados', help_text='Identificador deL interesado (COL).')
    tipo = models.ForeignKey(CR_InteresadoTipo, on_delete=models.PROTECT, verbose_name='Tipo de interesado', related_name='interesados', help_text='Persona natural que actúa a nombre propio ó persona juridica que actúa como institución', blank=False, null=False)
    tipo_documento = models.ForeignKey(CR_DocumentoTipo, on_delete=models.PROTECT, verbose_name='Tipo de documento', related_name='interesados_con_tipo_documento', blank=False, null=False)
    documento_identidad = models.CharField('Documento de identidad', max_length=50, unique=True, blank=False, null=False)
    primer_nombre = models.CharField('Primer nombre', max_length=200, blank=True, null=True, help_text='Primer nombre de la persona interesado en trámite o proceso.')
    segundo_nombre = models.CharField('Segundo nombre', max_length=200, blank=True, null=True, help_text='Segundo nombre de la persona interesado en trámite o proceso.')
    primer_apellido = models.CharField('Primer apellido', max_length=200, blank=True, null=True, help_text='Primer apellido de la persona interesado en trámite o proceso.')
    segundo_apellido = models.CharField('Segundo apellido', max_length=200, blank=True, null=True, help_text='Segundo apellido de la persona interesado en trámite o proceso.')
    sexo = models.ForeignKey(CR_SexoTipo, on_delete=models.SET_NULL, verbose_name='Tipo de sexo', related_name='interesados_sexo', blank=True, null=True)
    grupo_etnico = models.ForeignKey(CR_GrupoEtnicoTipo, on_delete=models.SET_NULL, verbose_name='Tipo de grupo étnico', related_name='interesados_grupo_etnico', blank=True, null=True)
    razon_social = models.CharField('Razón Social', max_length=200, blank=True, null=True, help_text='Nombre de la razón social cuando el interesado es de tipo juridica.')

    class Meta:
        """Meta definition for CR_Interesado."""

        verbose_name = 'Interesado (CR)'
        verbose_name_plural = 'Interesados (CR)'

    def __str__(self):
        """Unicode representation of CR_Interesado."""
        if self.razon_social:
            return self.razon_social
        return f"{self.primer_nombre or ''} {self.segundo_nombre or ''} {self.primer_apellido or ''} {self.segundo_apellido}".strip()

class COL_AgrupacionInteresados(BaseModel):
    """Model definition for COL_AgrupacionesInteresados."""

    # TODO: Define fields here
    interesado = models.OneToOneField(COL_Interesado, on_delete=models.CASCADE, verbose_name='ID Interesado', related_name='agrupacion_interesados', help_text='Identificador del interesado (COL).')
    tipo = models.ForeignKey(COL_GrupoInteresadoTipo, on_delete=models.PROTECT, verbose_name='Tipo de grupo de interesados', help_text='Indica el tipo de agrupación del que se trata', blank=False, null=False)

    class Meta:
        """Meta definition for COL_AgrupacionesInteresados."""

        verbose_name = 'Agrupación de interesados (COL)'
        verbose_name_plural = 'Agrupaciones de interesados (COL)'

    def __str__(self):
        """Unicode representation of COL_AgrupacionesInteresados."""
        return f"Agrupación de interesados: {self.tipo}" if self.tipo else "Agrupación sin tipo"

class col_miembros(BaseModel):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    interesado = models.ForeignKey(COL_Interesado, on_delete=models.CASCADE, related_name='miembro_agrupaciones')
    agrupacion = models.ForeignKey(COL_AgrupacionInteresados, on_delete=models.CASCADE, related_name='miembros_asociados')
    participacion = models.DecimalField('Participación', max_digits=5, decimal_places=2, blank=True, null=True, help_text='Proporción de la participación de interesado en la agrupación de la que hace parte.')

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'
            
    def __str__(self):
        return f"Interesados: {self.interesado}, Agrupación: {self.agrupacion}"


class CR_AgrupacionInteresados(BaseModel):
    """Model definition for CR_AgrupacionInteresados."""

    # TODO: Define fields here
    agrupacion_interesados = models.OneToOneField(COL_AgrupacionInteresados, on_delete=models.CASCADE, verbose_name='ID Agrupación de Interesados', related_name='Agrupaciones', help_text='Identificador de la agrupación(COL).')

    class Meta:
        """Meta definition for CR_AgrupacionInteresados."""

        verbose_name = 'Agrupación de Interesados (CR)'
        verbose_name_plural = 'Agrupaciones de interesados (CR)'

    def __str__(self):
        """Unicode representation of CR_AgrupacionInteresados."""
        return super().__str__()
    
class LC_InteresadoContacto(BaseModel):
    """Model definition for LC_InteresadoContacto."""

    # TODO: Define fields here
    interesado = models.ForeignKey(CR_Interesado, on_delete=models.CASCADE, related_name='contactos', verbose_name='Interesado')
    telefono = models.CharField('Telefono', max_length=50, blank=True, null=True, help_text='Número de telefono de contacto del interesado')
    domicilio_notificacion = models.CharField('Domicilio de notificación', max_length=150, blank=True, null=True, help_text='Domiciolo de notificación del interesado')
    direccion_notificacion = models.CharField('Dirección de residencia', max_length=150, blank=True, null=True, help_text='Dirección de residencia del interesado')
    correo_electronico = models.CharField('Correo electronico', max_length=150, blank=True, null=True, help_text='Correo electronio del interesado')
    autoriza_notificacion_correo = models.BooleanField('Autoriza notifiación por correo', default=False, blank=True, null=True)
    departamento = models.CharField('Departamento', max_length=100, blank=True, null=True, help_text='Departamento donde se encuentra el interesado')
    municipio = models.CharField('Municipio', max_length=100, blank=True, null=True, help_text='Municipio donde se enceuntra el interesado')
        
    class Meta:
        """Meta definition for LC_InteresadoContacto."""

        verbose_name = 'Contacto del interesado'
        verbose_name_plural = 'Contactos de los interesados'

    def __str__(self):
        """Unicode representation of LC_InteresadoContacto."""
        return self.correo_electronico or f"Contacto #{self.id}"



