from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
from apps.estructuras.models import ExtArchivo
from apps.dominios.models import COL_EstadoDisponibilidadTipo, CI_Forma_Presentacion_Codigo, COL_FuenteAdministrativaTipo, LC_FuenteAdministrativaTipo, COL_FuenteEspacialTipo

# Create your models here.
class COL_Fuente(BaseModel):
    """Model definition for COL_FUENTE."""

    # TODO: Define fields here
    estado_disponibilidad = models.ForeignKey(COL_EstadoDisponibilidadTipo, on_delete=models.PROTECT, verbose_name='Estado de disponibilidad', related_name='fuentes', help_text='Indica si la fuente está o no disponible y en qué condiciones', blank=False, null=False)
    ext_archivo_id = models.OneToOneField(ExtArchivo, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Ext archivo id', related_name='col_fuente', help_text='Identificador del archivo fuente controlado por una clase externa')
    tipo_principal = models.ForeignKey(CI_Forma_Presentacion_Codigo, on_delete=models.SET_NULL, verbose_name='Tipo principal', related_name='fuentes', help_text='Tipo de formato en el que es presentada la fuente', blank=True, null=True)
    fecha_documento_fuente = models.DateField('Fecha de documento fuente', auto_now=False, auto_now_add=False, blank=True, null=True, help_text='Fecha de expedición del documento fuente')

    class Meta:
        """Meta definition for COL_FUENTE."""

        verbose_name = 'Fuente'
        verbose_name_plural = 'Fuentes'

    def __str__(self):
        """Unicode representation of COL_FUENTE."""
        return f"Fuente: {self.estado_disponibilidad}"
    
class COL_FuenteAdministrativa(BaseModel):
    """Model definition for COL_FuenteAdministrativa."""

    # TODO: Define fields here
    fuente = models.OneToOneField(COL_Fuente, on_delete=models.CASCADE, verbose_name='ID Fuente', related_name='fuentes_administrativas', help_text='Id de la fuente.')
    observacion = models.CharField('Observación', max_length=250, blank=True, null=True, help_text='Observaciones o descripciones del documento de la fuente administrativa')
    tipo = models.ForeignKey(COL_FuenteAdministrativaTipo, on_delete=models.PROTECT, verbose_name='Tipo', related_name='Fuente_COL', help_text='Tipo de documento de fuente administrativa', blank=False, null=False)
    numero_fuente = models.CharField('Número de fuente', max_length=50, blank=True, null=True, help_text='Identificador del documento (número de resolución, escritura pública, radicado de una sentencia)')

    class Meta:
        """Meta definition for COL_FuenteAdministrativa."""

        verbose_name = 'Fuente Administrativa (COL)'
        verbose_name_plural = 'Fuentes Administrativas (COL)'

    def __str__(self):
        """Unicode representation of COL_FuenteAdministrativa."""
        return f"{self.tipo} - {self.numero_fuente}"
    
class LC_FuenteAdministrativa(BaseModel):
    """Model definition for LC_FuenteAdministrativa."""

    # TODO: Define fields here
    fuente_administrativa = models.OneToOneField(COL_FuenteAdministrativa, on_delete=models.CASCADE, verbose_name='ID Fuente Administrativa', related_name='fuentes_administrativasLC', help_text='Id de la fuente administrativa.')
    tipo_documento = models.ForeignKey(LC_FuenteAdministrativaTipo, on_delete=models.PROTECT, verbose_name='Tipo de documento', related_name='Fuente_CR', help_text='Documento que acredita la adquisición de derechos de dominio sobre un inmueble', blank=False, null=False)
    ente_emisor = models.CharField('Ente emisor', max_length=200, blank=True, null=True, help_text='Entidades encargadas de mitir el título de dominio, posesión u ocupación.')

    class Meta:
        """Meta definition for LC_FuenteAdministrativa."""

        verbose_name = 'Fuente Administrativa (LC)'
        verbose_name_plural = 'Fuentes Administrativas (LC)'

    def __str__(self):
        """Unicode representation of LC_FuenteAdministrativa."""
        return self.tipo
    
class COL_FuenteEspacial(BaseModel):
    """Model definition for COL_FuenteESpacial."""

    # TODO: Define fields here
    fuente = models.OneToOneField(COL_Fuente, on_delete=models.CASCADE, verbose_name='ID Fuente', related_name='FuenteEspacial_COL', help_text='Id de la fuente.')
    nombre = models.CharField('Nombre', max_length=100, blank=False, null=False, help_text='Nombre de la fuente espacial del levantamiento catastral de un predio.')
    tipo = models.ForeignKey(COL_FuenteEspacialTipo, on_delete=models.PROTECT, verbose_name='Tipo', related_name='FuenteEspacial_COL', help_text='Tipo de fuente espacial.', blank=False, null=False)
    descripcion = models.CharField('Descripción', max_length=250, blank=True, null=True, help_text='Descripción de la fuente espacial.')
    metadato = models.CharField('Metadata', max_length=250, blank=True, null=True, help_text='Metadato de la fuente espacial.')

    class Meta:
        """Meta definition for COL_FuenteESpacial."""

        verbose_name = 'Fuente Espacial (COL)'
        verbose_name_plural = 'Fuentes Espaciales (COL)'

    def __str__(self):
        """Unicode representation of COL_FuenteESpacial."""
        return f"Fuente Espacial: {self.nombre} - {self.tipo}"
    
class CR_FuenteEspacial(BaseModel):
    """Model definition for CR_FuenteEspacial."""

    # TODO: Define fields here
    fuente_espacial = models.OneToOneField(COL_FuenteEspacial, on_delete=models.CASCADE, verbose_name='ID Fuente Espacial', related_name='FuenteEspacial_CR', help_text='Id de la fuente espacial.')
    tipo = models.ForeignKey(COL_FuenteEspacialTipo, on_delete=models.PROTECT,verbose_name='Tipo', related_name='FuenteEspacial_CR', help_text='Insumos utilizados para la obtención de infromación espacial', blank=False, null=True)
    metadato_FE = models.CharField('Metadato', max_length=250, blank=True, null=True, help_text='Corresponde a la ficha técnica y especificaciones del insumo utlizado para el levantamiento catastral.')

    class Meta:
        """Meta definition for CR_FuenteEspacial."""

        verbose_name = 'Fuente Espacial (CR)'
        verbose_name_plural = 'Fuentes Espaciales (CR)'

    def __str__(self):
        """Unicode representation of CR_FuenteEspacial."""
        return f"Fuente Espacial CR: {self.tipo}"




