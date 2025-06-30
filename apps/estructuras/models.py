from django.db import models
from django.contrib.gis.db import models as gis_models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
from apps.dominios.models import TipoDireccionTipo, ClaseViaPrincipalClase, SectorTipo, TipoNovedadTipo, TipoNovedadFMITipo, COL_AreaTipo, COL_VolumenTipo, GeometriaClase

# Create your models here.
class ExtDireccion(BaseModel):
    """Model definition for ExtDireccion."""

    # TODO: Define fields here
    
    id_direccion = models.CharField('ID de Dirección', max_length=50, unique=True, blank=False, null=False, help_text='Identificador único de la dirección.')
    predio = models.ForeignKey('paquete_administrativo.LC_Predio', on_delete=models.CASCADE, blank=True, null=True, related_name='direcciones', verbose_name='predio')
    tipo_direccion = models.ForeignKey(TipoDireccionTipo, on_delete=models.PROTECT, blank=False, null=False, verbose_name='Tipo de dirección', related_name='direcciones')
    es_direccion_principal = models.BooleanField('¿Es dirección principal?', blank=True, null=True, help_text='Indica si esta es la dirección principal del predio')
    codigo_postal = models.CharField('Código postal', max_length=50, blank=True, null=True, help_text='Código postal asociado a la dirección')
    clase_via_principal = models.ForeignKey(ClaseViaPrincipalClase, on_delete=models.PROTECT, blank=True, null=True, related_name='direcciones')
    valor_via_principal = models.CharField('Valor vía principal', max_length=50, blank=True, null=True)
    letra_via_principal = models.CharField('Letra vía principal', max_length=50, blank=True, null=True )
    letra_via_generadora = models.CharField('Letra de vía generadora', max_length=50, blank=True, null=True)
    sector_ciudad = models.ForeignKey(SectorTipo, on_delete=models.PROTECT, blank=True, null=True, related_name='ciudades', help_text='Sector de la ciudad')
    valor_via_generadora = models.CharField('Valor de vía generadora', max_length=50, blank=True, null=True)
    numero_predio = models.CharField('Número del predio', max_length=50, blank=True, null=True)
    sector_predio = models.ForeignKey(SectorTipo, on_delete=models.PROTECT, blank=True, null=True, related_name='predios', help_text='Sector del predio')
    complemento = models.CharField('Complemento', max_length=200, blank=True, null=True, help_text='Información adicional sobre la dirección')
    nombre_predio = models.CharField('Nombre del predio', max_length=200, blank=True, null=True, help_text='Nombre de los predios en el sector rual. ESte valor se diligencia cuando el tipo de direccion es No Estructurada')
    localizacion = gis_models.PointField('Localización',blank=True, null=True, help_text='Par de valores georreferenciados (x,y) en los que se encuentra la dirección')


    class Meta:
        """Meta definition for ExtDireccion."""

        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'

    def __str__(self):
        """Unicode representation of ExtDireccion."""
        return self.id_direccion
    
class LC_EstructuraNovedadNumeroPredial(BaseModel):
    """Model definition for LC_EstructuraNovedadNumeroPredial."""

    # TODO: Define fields here
    id_novedad_numero_predial = models.CharField('ID Novedad Número Predial', max_length=50, unique=True, blank=False, null=False, help_text='Identificador único de la novedad de número predial.')
    numero_predial = models.CharField('Número predial', max_length=30, blank=False, null=False, help_text='El predio no sufre modificación del código predial nacional de 30 dígitos de acuerdo con la estructura')
    tipo_novedad = models.ForeignKey(TipoNovedadTipo, on_delete=models.PROTECT, blank=False, null=False, verbose_name='Tipo de novedad', related_name='novedades')

    class Meta:
        """Meta definition for LC_EstructuraNovedadNumeroPredial."""

        verbose_name = 'Novedad número predial'
        verbose_name_plural = 'Novedades número predial'

    def __str__(self):
        """Unicode representation of LC_EstructuraNovedadNumeroPredial."""
        return self.id_novedad_numero_predial
    
class LC_NovedadFMI(BaseModel):
    """Model definition for LC_NovedadFMI."""

    # TODO: Define fields here
    id_novedad_FMI = models.CharField('ID de Novedad FMI', max_length=50, unique=True, blank=False, null=False, help_text='Identificador único de la novedad de FMI.')
    codigo_ORIP = models.CharField('Código ORIP', max_length=50, blank=False, null=False, help_text='ES el consecutivo que se asigna a cada oficina de registro de instrumentos públicos')
    numero_FMI = models.CharField('Número FMI', max_length=50, blank=False, null=False, help_text='Es el consecutivo que se asigna a cada predio juridico abierto en la ORIP')
    tipo_novedadFMI = models.ForeignKey(TipoNovedadFMITipo, on_delete=models.PROTECT, blank=False, null=False, verbose_name='Tipo de novedad', related_name='novedades_fmi')

    class Meta:
        """Meta definition for LC_NovedadFMI."""

        verbose_name = 'Novedad FMI'
        verbose_name_plural = 'Novedades FMI'

    def __str__(self):
        """Unicode representation of LC_NovedadFMI."""
        return self.id_novedad_FMI
    
class ExtInteresado(BaseModel):
    """Model definition for ExtInteresado."""

    # TODO: Define fields here
    id_interesado = models.CharField('ID de Interesado', max_length=50, unique=True, blank=False, null=False, help_text='Identificador único del interesado.')
    ext_direccion = models.ForeignKey(ExtDireccion, on_delete=models.SET_NULL,related_name='interesados',blank=True, null=True, verbose_name='Dirección')
    huella_dactilar = models.CharField('Huella Dactilar',  max_length=200, blank=True, null=True, help_text='Imagen de la huella dactilar del interesado.')
    nombre = models.CharField('Nombre', max_length=200, blank=True, null=True, help_text='Campo de nombre del interesado.')
    fotografia = models.CharField('Fotografía', max_length=200, blank=True, null=True, help_text='Fotografía del interesado.')
    firma = models.CharField('Firma', max_length=200, blank=True, null=True, help_text='Firma del interesado.')
    documento_escaneado = models.CharField('Documento escaneado', max_length=200, blank=True, null=True, help_text='Ruta de almacenamiento del documento escaneado del interesado.')

    class Meta:
        """Meta definition for ExtInteresado."""

        verbose_name = 'Información de interesado'
        verbose_name_plural = 'Información de interesados'

    def __str__(self):
        """Unicode representation of ExtInteresado."""
        return self.id_interesado
    
class ExtArchivo(BaseModel):
    """Model definition for ExtArchivo."""

    # TODO: Define fields here

    fecha_aceptacion = models.DateField('Fecha de aceptación', auto_now=False, auto_now_add=False, blank=True, null=True, help_text='Fecha en la que ha sido aceptado el documento.')
    datos = models.CharField('Datos', max_length=250, blank=True, null=True, help_text='Datos que contiene el documento.')
    extraccion = models.DateField('Extracción', auto_now=False, auto_now_add=False, blank=True, null=True, help_text='Última fecha de extracción del documento.')
    fecha_grabacion = models.DateField('Fecha de grabación', auto_now=False, auto_now_add=False, blank=True, null=True, help_text='Fecha en la que el documento es aceptado en el sistema.')
    fecha_entrega = models.DateField('Fecha de entrega', auto_now=False, auto_now_add=False, blank=True, null=True, help_text='Fecha en la que fue entregado el documento.')
    espacio_de_nombres = models.CharField('Espacio de nombres', max_length=50, unique=True, blank=False, null=False, help_text='Identificador único global. Corresponde al atributo de la clase en LADM.')
    local_id = models.CharField('Local ID', max_length=50, unique=True, blank=False, null=False, help_text='Identificador único local.')


    class Meta:
        """Meta definition for ExtArchivo."""

        verbose_name = 'Repositorio de archivo'
        verbose_name_plural = 'Repositorios de archivos'

    def __str__(self):
        """Unicode representation of ExtArchivo."""
        return f"Archivo {self.local_id}"
    
class COL_AreaValor(BaseModel):
    """Model definition for COL_AreaValor."""

    # TODO: Define fields here
    id_area_valor = models.CharField('ID de Valor de área', max_length=50, unique=True, blank=False, null=False, help_text='Identificador único del valor de área.')
    tipo = models.ForeignKey(COL_AreaTipo, on_delete=models.PROTECT, blank=False, null=False, related_name='tipo_area', verbose_name='Tipo', help_text='Indica si el valor a registra corresonde al área geográfica o alfanumérica de la base de datos catastral.')
    area = models.DecimalField('Àrea', max_digits=15, decimal_places=2, blank=False, null=False, help_text='Corresponde al valor del área registral en la base de datos catastral.')
    datos_proyeccion = models.CharField('Datos de la proyecciòn', max_length=250, blank=True, null=True, help_text='Parametros de la proyección utilizada para el cálculo del área.')

    class Meta:
        """Meta definition for COL_AreaValor."""

        verbose_name = 'Valor de área'
        verbose_name_plural = 'Valores de área'

    def __str__(self):
        """Unicode representation of COL_AreaValor."""
        return f"{self.id} - {self.id_area_valor}"
        
class COL_VolumenValor(BaseModel):
    """Model definition for COL_VolumenValor."""

    # TODO: Define fields here
    id_volumen_valor = models.CharField('ID de Valor de volumen', max_length=50, unique=True, blank=False, null=False, help_text="Identificador único del valor de volumen.")
    volumen_medicion = models.DecimalField('Volumen medición', max_digits=15, decimal_places=2, blank=False, null=False, help_text='Medición del volumen en m3.')
    tipo = models.ForeignKey(COL_VolumenTipo, on_delete=models.PROTECT, blank=False, null=False, related_name='tipo_volumen', verbose_name='Tipo', help_text='Indicación de si el volumen es calculado, si figura como oficial o si se da otra circunstancia.')

    class Meta:
        """Meta definition for COL_VolumenValor."""

        verbose_name = 'Valor de volumen'
        verbose_name_plural = 'Valores de volumen'

    def __str__(self):
        """Unicode representation of COL_VolumenValor."""
        return f"{self.id} - {self.id_volumen_valor}"
    
class GM_MultiSurface3D(BaseModel):
    """Model definition for GM_MultiSurface3D."""

    # TODO: Define fields here
    id_geometria = models.CharField('ID Geometría', max_length=50, unique=True, blank=False, null=False, help_text='Identificador único de la geometría. Terreno (T), Construcción (C), Únidad de Construcción (UC)')
    clase_geometria = models.ForeignKey(GeometriaClase, on_delete=models.PROTECT, blank=False, null=False, related_name='clase_geoemetria', verbose_name='Clase', help_text='Indicación a que clase pertenece la geometría (Terreno, Construcción, Únidad de construcción')
    geometria = gis_models.MultiPolygonField('Geometría', blank=False, null=False, help_text='Corresponde a la figura geométrica vectorial poligonal, generada a partir de los linderos del predio, linderos de la construcción o de la únidad de construcción.')

    class Meta:        
        """Meta definition for GM_MultiSurface3D."""

        verbose_name = 'Geometría'
        verbose_name_plural = 'Geometrias'

    def __str__(self):
        """Unicode representation of GM_MultiSurface3D."""
        return self.id_geometria








