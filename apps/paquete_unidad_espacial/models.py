from django.db import models
from django.contrib.gis.db import models as gis_models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
from apps.estructuras.models import COL_AreaValor, ExtDireccion, COL_VolumenValor, GM_MultiSurface3D
from apps.dominios.models import COL_DimensionTipo, COL_RelacionSuperficieTipo, CR_ConstruccionPlantaTipo, CR_UnidadConstruccionTipo, CR_UsoUConsTipo

# Create your models here.
class COL_UnidadEspacial(BaseModel):
    """Model definition for COL_."""

    # TODO: Define fields here
    area = models.ManyToManyField(COL_AreaValor, blank=True, verbose_name='Área', related_name='unidades_espaciales', help_text='Registro del área en diferente sistemas.')
    dimension = models.ForeignKey(COL_DimensionTipo, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Dimensión', related_name='unidades_espaciales', help_text='Dimensión del objeto.')
    ext_direccion_id = models.ManyToManyField(ExtDireccion, blank=True, verbose_name='Ext direccion id', related_name='unidades_espaciales', help_text='Corresponde al atributo extAddresID de la clase en LADM.')
    etiqueta = models.CharField('Etiqueta', max_length=50, blank=True, null=True, help_text='Corresponde al atributo label de la clase en LADM.')
    relacion_superficie = models.ForeignKey(COL_RelacionSuperficieTipo, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Relación superficie', related_name='unidades_espaciales', help_text='Corresponde al atributo surfaceRelation de la clase en LADM.')
    volumen = models.ManyToManyField(COL_VolumenValor, blank=True, verbose_name='Volumen', related_name='unidades_espaciales', help_text='Corresponde al atributo volumen de la clase en LADM.')
    #geometria = gis_models.MultiPolygonField('Geometría', blank=False, null=False, help_text='Almacena de forma permanente la geometría de tipo poligonal')

    class Meta:
        """Meta definition for COL_."""

        verbose_name = 'Unidad Espacial'
        verbose_name_plural = 'Unidades Espaciales'

    def __str__(self):
        """Unicode representation of COL_."""
        return self.etiqueta if self.etiqueta else f"Unidad Espacial {self.pk}"
    
class CR_Construccion(BaseModel):
    """Model definition for CR_Construccion."""

    # TODO: Define fields here
    unidad_espacial = models.OneToOneField(COL_UnidadEspacial, on_delete=models.CASCADE, verbose_name='ID Unidad Espacial', related_name='construcciones', help_text='Identificador de la unidad de construcción.')
    identificador = models.CharField('Identificador', max_length=50, unique=True, blank=True, null=True, help_text='Identificador de la unidad de construcción, su codificación puede ser por letras del abecedario.')
    total_pisos = models.PositiveIntegerField('Total Pisos', blank=False, null=False, help_text='Número total de pisos de la construcción.')
    total_sotanos = models.PositiveIntegerField('Total Sótanos', blank=True, null=True, help_text='Número total de sótanos de la construcción.')
    total_mezanines = models.PositiveIntegerField('Total Mezanines', blank=True, null=True, help_text='Número total de mezanines de la construcción.')
    total_semisotanos = models.PositiveIntegerField('Total Semisotanos', blank=True, null=True, help_text='Número total de semisótanos de la construcción.')
    area_total_construccion = models.DecimalField('Área Total Construcción ', max_digits=15, decimal_places=2, blank=False, null=False, help_text='Àrea total construida.')
    altura_total_construccion = models.DecimalField('Altura  Total Construcción', max_digits=15, decimal_places=2, blank=True, null=True, help_text='Altura total de la construcción.')
    construccion_geometria = gis_models.MultiPolygonField('Geometría Construcción', srid=9377, blank=True, null=True, help_text='Corresponde a la figura geometrica vectorial poligonal, generada a partir de los linderos del predio.')

    class Meta:
        """Meta definition for CR_Construccion."""

        verbose_name = 'Construcción'
        verbose_name_plural = 'Construcciones'

    def __str__(self):
        """Unicode representation of CR_Construccion."""
        return f"COnstrucción {self.identificador}"

class CR_CaracteristicasUnidadConstruccion(BaseModel):
    """Model definition for CR_CaracteristicasUnidadConstruccion."""

    # TODO: Define fields here
    identificador = models.CharField('Identificador', max_length=50, blank=False, null=False, unique=True, help_text='Identificador de la unidad de construcción, su codificación puede ser por letras del abecedario.')
    tipo_unidad_construccion = models.ForeignKey(CR_UnidadConstruccionTipo, on_delete=models.PROTECT, blank=False, null=False, verbose_name='Tipo de unidad de construcción', related_name='Caracteristicas_UC', help_text='Conjunto de elementos constructivos que conforman una edificación.')
    total_plantas = models.PositiveIntegerField('Total de plantas', blank=True, null=True, help_text='Número total de plantas en la unidad de construcción.')
    uso = models.ForeignKey(CR_UsoUConsTipo, on_delete=models.PROTECT, blank=False, null=False, related_name='caracteristicas_UC', verbose_name='Uso', help_text='Destinación de los materiales de una unidad construcitiva con respecto a la actividad económica.')
    anio_construccion = models.PositiveIntegerField('Año de construcción', blank=True, null=True, help_text='Año de construcción de la unidad constructiva.')
    area_construida = models.DecimalField('Área construida', max_digits=15, decimal_places=2, blank=False, null=False, help_text='Área total constuida en la unidad de construcción.')
    area_privada_construida = models.DecimalField('área privada construida', max_digits=15, decimal_places=2, blank=True, null=True, help_text='Àrea total privada de la unidad de construcción para los predios en régimen de propiedad horizontal.')
    observaciones = models.CharField('Observaciones', blank=True, null=True, help_text='Observaciones generales respecto de la unidad de construcción.')

    class Meta:
        """Meta definition for CR_CaracteristicasUnidadConstruccion."""

        verbose_name = 'Caracteristica Unidad de construcción'
        verbose_name_plural = 'Caracteristicas Unidades de construcción'

    def __str__(self):
        """Unicode representation of CR_CaracteristicasUnidadConstruccion."""
        return f"Características de Unidad {self.identificador}"

class CR_UnidadConstruccion(BaseModel):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    unidad_espacial = models.OneToOneField(COL_UnidadEspacial, on_delete=models.CASCADE, verbose_name='ID Unidad Espacial', related_name='unidades_construcciones', help_text='Identificador de la unidad de construcción.')
    construccion = models.ForeignKey(CR_Construccion, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Construcción', related_name='uniddades_construccion', help_text='Construccioón a la que pertenece esta unidad.')
    caracteristicas = models.ForeignKey(CR_CaracteristicasUnidadConstruccion, on_delete=models.CASCADE, verbose_name='Caracteristicas', related_name='unidades_construccion', help_text='Caracteristicas asociadas a la unidad de construcción.')
    tipo_planta = models.ForeignKey(CR_ConstruccionPlantaTipo, on_delete=models.PROTECT, blank=False, null=False, verbose_name='Tipo de planta', related_name='unidades_construccion', help_text='Indica el tipo de planta donde se ubica la unidad de construcción.')
    planta_ubicacion = models.PositiveIntegerField('Ubicación de la planta',blank=False, null=False, help_text='Indica númericamente la ubicación de la planta')
    area_construida = models.DecimalField('Área construida de la planta', max_digits=15, decimal_places=2, blank=False, null=False, help_text='Área total construida en la unidad de construcción.')
    altura = models.DecimalField('Altura de la planta', max_digits=15, decimal_places=2, blank=True, null=True, help_text='Altura total de la planta.')
    unidad_construccion_geometria = gis_models.MultiPolygonField('Geometría Unidad Construcción', srid=9377, blank=True, null=True, help_text='Corresponde a la figura geometrica vectorial poligonal, generada a partir de los linderos del predio.')

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Unidad de construcción'
        verbose_name_plural = 'Unidades de construcción'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return f"Unidad de construccion en planta {self.planta_ubicacion}"

class CR_Terreno(BaseModel):
    """Model definition for CR_Terreno."""

    # TODO: Define fields here
    unidad_espacial = models.OneToOneField(COL_UnidadEspacial, on_delete=models.CASCADE, verbose_name='ID Unidad Espacial', related_name='terrenos', help_text='Identificador de la unidad de construcción.')
    area_terreno = models.DecimalField('Área de terreno', max_digits=15, decimal_places=2, blank=False, null= False, help_text='Àrea total del terreno resultante del levantamiento catastral.')
    terreno_geometria = gis_models.MultiPolygonField('Geometría Terreno',srid=9377, blank=True, null=True, help_text='Corresponde a la figura geometrica vectorial poligonal, generada a partir de los linderos del predio.')


    class Meta:
        """Meta definition for CR_Terreno."""

        verbose_name = 'Terreno'
        verbose_name_plural = 'Terrenos'

    def __str__(self):
        """Unicode representation of CR_Terreno."""
        return f"Terreno con area de {self.area_terreno} m2"



