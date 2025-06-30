from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
from apps.dominios.models import COL_UnidadAdministrativaBasicaTipo, LC_PredioTipo, LC_CondicionPredioTipo, LC_DestinacionEconomicaTipo, LC_ResultadoVisitaTipo, CR_DocumentoTipo, LC_DerechoTipo
from apps.estructuras.models import ExtDireccion, LC_EstructuraNovedadNumeroPredial, LC_NovedadFMI

# Create your models here.
class COL_UnidadAdministrativaBasica(BaseModel):
    """Model definition for COL_UnidadAdministrativaBasica."""

    # TODO: Define fields here
    nombre = models.CharField('Nombre', max_length=200, unique=True, blank= True, null=True, help_text='Nombre que recibe la unidad administrativa básica, en muchos casos toponímico, especialmente en terrenos rústicos.')
    tipo_UAB = models.ForeignKey(COL_UnidadAdministrativaBasicaTipo, on_delete=models.PROTECT, verbose_name='Tipo UAB', related_name='unidades_administrativas', help_text='Tipo de derecho que la reconoce a la unidad administrativa básica.')

    class Meta:
        """Meta definition for COL_UnidadAdministrativaBasica."""

        verbose_name = 'Unidad Administrativa Básica'
        verbose_name_plural = 'Unidades Administrativas Básicas'

    def __str__(self):
        """Unicode representation of COL_UnidadAdministrativaBasica."""
        return self.nombre or "Unidad Administrativa Sin Nombre"

class LC_Predio(BaseModel):
    """Model definition for LC_Predio."""

    # TODO: Define fields here
    unidad_basica_administrativa = models.OneToOneField(COL_UnidadAdministrativaBasica, on_delete=models.CASCADE, verbose_name='ID Unidad Básica Administrativa', related_name='predio', help_text='Identificador de la Únidad Basica Administrativa')
    departamento = models.CharField('Departamento', max_length=100, blank=False, null=False, help_text='Corresponde al código del Departamento al cual pertenece el predio. Es asignado por DIVIPOLA y tiene 2 dígitos.')
    municipio = models.CharField('Municipio', max_length=100, blank=False, null=False, help_text='Corresponde al código del municipio al cual pertenece el predio. Es asignado por DIVIPOLA y tiene 3 dígitos.')
    direccion = models.ForeignKey(ExtDireccion, on_delete=models.CASCADE, related_name='predios', blank=False, null=False, verbose_name='Direcciòn')
    id_operacion = models.CharField('ID de Operación', max_length=50, unique=True, blank=False, null=False, help_text='Identificador úncio temporal del predio en el levantamiento catastral')
    codigo_orip = models.CharField('Código ORIP', max_length=50, blank=True, null=True, help_text='Circulo registral')
    matricula_inmobiliaria = models.CharField('Matrícula inmobiliaria', max_length=50, blank=True, null=True, help_text='Matricula inmobiliaria')
    numero_predial = models.CharField('Número Predial', max_length=30, blank=True, null=True, help_text='Nuevo código numérico de treinta (30) digitos, que se le asigna a cada predio')
    codigo_homologado = models.CharField('Código homologado', max_length=50, blank=True, null=True, help_text='Es un código único para identificar los inmuebles tanto en los sistemas de información catastral como registral')
    avaluo_catastral = models.DecimalField('Avalúo Catastral', max_digits=15, decimal_places=2, blank=True, null=True, help_text='Valor del avalúo catastral del predio')
    tipo = models.ForeignKey(LC_PredioTipo, on_delete=models.PROTECT, verbose_name='Tipo de predio', related_name='predios',help_text='Indica el tipo de predio para efectos catastrales')
    condicion_predio = models.ForeignKey(LC_CondicionPredioTipo, on_delete=models.PROTECT, verbose_name='Condición del predio', related_name='predios', help_text='Caracterización temática de las condiciones del predio')
    destinacion_economica = models.ForeignKey(LC_DestinacionEconomicaTipo, on_delete=models.PROTECT, verbose_name='Destinación económica', related_name='predios', help_text='Clasificación para fines estadisticos y económicos que se da a cada inmueble')
    lc_predio_copropiedad = models.ManyToManyField('self',through='cr_predio_copropiedad', symmetrical=False, blank=True, related_name='copropiedades', verbose_name='copropiedades')
    lc_predio_informalidad = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='informalidades', verbose_name='Predios relacionados por informalidad', help_text='Asocia predios relacionados por informalidad', limit_choices_to={'condicion_predio':9})

    class Meta:
        """Meta definition for LC_Predio."""

        verbose_name = 'Predio'
        verbose_name_plural = 'Predios'

    def __str__(self):
        """Unicode representation of LC_Predio."""
        return f"{self.id_operacion}"

class cr_predio_copropiedad(BaseModel):
    """Model definition for cr_predio_copropiedad."""

    # TODO: Define fields here
    predio_matriz = models.ForeignKey(LC_Predio, related_name='copropiedades_matriz',on_delete=models.CASCADE, limit_choices_to=models.Q(condicion_predio=2) | models.Q(condicion_predio=4) | models.Q(condicion_predio=6)) 
    unidad_predial = models.ForeignKey(LC_Predio,related_name='copropiedades_unidades', on_delete=models.CASCADE, limit_choices_to=models.Q(condicion_predio=3) | models.Q(condicion_predio=5) | models.Q(condicion_predio=7))
    coeficiente = models.FloatField('Coeficiente', blank=True, null=True, help_text='Coeficiente de copropiedad de la unidad predial')

    class Meta:
        """Meta definition for cr_predio_copropiedad."""

        verbose_name = 'Predio en Copropiedad'
        verbose_name_plural = 'Predios en Copropiedad'

    def __str__(self):
        """Unicode representation of cr_predio_copropiedad."""
        return f"Predio matriz: {self.predio_matriz}, Unidad predial: {self.unidad_predial}"

class CR_DatosPHCondominio(BaseModel):
    """Model definition for CR_DatosPHCondominio."""

    # TODO: Define fields here
    predio = models.OneToOneField('LC_Predio', on_delete=models.CASCADE, related_name='datos_ph_condominio', verbose_name='Predio asociado')
    area_total_terreno = models.FloatField('Área total de terreno', blank=True, null=True, help_text='Área total del terreno del PH o Condominio Matriz')
    area_total_terreno_privada = models.FloatField('Área total de terreno privada', blank=True, null=True, help_text='Área total privada del terreno del PH o Condominio Matriz')
    area_total_comun = models.FloatField('Área total de terreno común', blank=True, null=True, help_text='Área total de terreno común del PH o Condomino Matriz')
    area_total_construida = models.FloatField('Área total construida', blank=True, null=True, help_text='Área total de construida del PH o Condominio Matriz')
    area_total_construida_privada = models.FloatField('Área total construida privada', blank=True, null=True, help_text='Área total construida privada del PH o Condominio Matriz')
    area_total_construida_comun = models.FloatField('Área total construida común', blank=True, null=True, help_text='Área total construida común del PH o Condominio Matriz')
    numero_torres = models.IntegerField('Número de torres', blank=True, null=True, help_text='Número de torrer en el Ph o Condominio')
    total_unidades_privadas = models.IntegerField('Total de unidades privadas', blank=True, null=True, help_text='Total de unidades privadas en el PH o COndominio')

    class Meta:
        """Meta definition for CR_DatosPHCondominio."""

        verbose_name = 'Datos de PH o Condominio'
        verbose_name_plural = 'Datos de PH o Condominios'

    def __str__(self):
        """Unicode representation of CR_DatosPHCondominio."""
        return f"PH/Condominio: {self.id}"

class LC_DatosAdicionalesLevantamientoCatastral(BaseModel):
    """Model definition for LC_DatosAdicionalesLevantamientoCatastral."""

    # TODO: Define fields here
    predio = models.OneToOneField('LC_PREDIO', on_delete=models.CASCADE,related_name='datos_adicionales', verbose_name='Predio Asociado')
    area_registral_m2 = models.FloatField('Área registral en metros cuadrados', blank=True, null=True, help_text='Área consignada en el CTL, descripción de cabidad y linderos o en titulos registrados en metros cuadrados')
    novedad_numeros_prediales = models.ForeignKey(LC_EstructuraNovedadNumeroPredial, on_delete=models.SET_NULL, related_name='predios_con_novedades', blank=True, null=True, verbose_name='Novedad números prediales')
    novedad_fmi = models.ForeignKey(LC_NovedadFMI, on_delete=models.SET_NULL, related_name='predios_con_novedades_fmi', blank=True, null=True, verbose_name='Novedad FMI')
    observaciones = models.TextField('Observaciones', blank=True, null=True, help_text='Observaciones generales respecto al predio')
    fecha_visita_predial = models.DateField('Fecha de visita predial', auto_now=False, auto_now_add=False, blank=True, null=True, help_text='Fecha de la visita en campo al predio')
    resultado_visita = models.ForeignKey(LC_ResultadoVisitaTipo, on_delete=models.PROTECT, blank=False, null=False, verbose_name='Resultado de la visita predial', related_name='visitas_prediales', help_text='Resultado obtenido tras la visita predial')

    class Meta:
        """Meta definition for LC_DatosAdicionalesLevantamientoCatastral."""

        verbose_name = 'Dato adicional de levantamiento catastral'
        verbose_name_plural = 'Datos adicionales de levantamiento catastral'

    def __str__(self):
        """Unicode representation of LC_DatosAdicionalesLevantamientoCatastral."""
        return f"Datos adicionales: {self.id}"
    
class LC_ContactoVisita(BaseModel):
    """Model definition for LC_ContactoVisita."""

    # TODO: Define fields here
    datos_adicionales = models.ForeignKey(LC_DatosAdicionalesLevantamientoCatastral, on_delete=models.CASCADE, related_name='contacto_visita', verbose_name='Datos adicionales Levantamiento Catastral')
    nombre_apellidos_quien_atendio = models.CharField('Nombre y apellidos de quien atendió', max_length=250, blank=False, null=False, help_text='Nombres y apellidos de la persona encargada de atender la visita')
    tipo_documento_quien_atendio = models.ForeignKey(CR_DocumentoTipo, on_delete=models.SET_NULL, related_name='contactos_con_tipo_documento', blank=True, null=True)
    numero_documento_quien_atendio = models.CharField('Número de documento de quien atendió la visita predial', max_length=50, blank=True, null=True)
    domicilio_notificaciones = models.CharField('Domicio notificaciones', max_length=200, blank=True, null=True)
    celular = models.CharField('Celular', max_length=50, blank=True, null=False, help_text='Número de celular de la persona que atendió la visita')
    correo_electronio = models.CharField('Correo Electronico', max_length=100, blank=True, null=True, help_text='Número de celular de la persona que atendió la visita')
    autoriza_notificaciones = models.BooleanField('Autoriza Notificaciones', default=False, blank=True, null=True)

    class Meta:
        """Meta definition for LC_ContactoVisita."""

        verbose_name = 'Contacto de Visita'
        verbose_name_plural = 'Contactos de visita'

    def __str__(self):
        """Unicode representation of LC_ContactoVisita."""
        return f"Contacto Visita: {self.nombre_apellidos_quien_atendio}"
    
class COL_DRR(BaseModel):
    """Model definition for COL_DRR."""

    # TODO: Define fields here
    col_baunitRrr = models.ForeignKey(COL_UnidadAdministrativaBasica, on_delete=models.CASCADE, related_name='drss', verbose_name='UAB') 
    descripcion = models.TextField('Descripción', blank=True, null=True, help_text='Descricpición asociada al derecho, la responsabilidad o la restricción')

    class Meta:
        """Meta definition for COL_DRR."""

        verbose_name = 'Derecho Responsabilidad y Restricción'
        verbose_name_plural = 'Derechos Responsabilidades y Restricciones'

    def __str__(self):
        """Unicode representation of COL_DRR."""
        return self.descripcion if self.descripcion else "Sin descripción"
    
class LC_Derecho(BaseModel):
    """Model definition for LC_Derecho."""

    # TODO: Define fields here
    DRR = models.OneToOneField(COL_DRR, on_delete=models.CASCADE, verbose_name='ID DRR', related_name='derechos', help_text='Identificador de Derechos, Responsabilidades y Restricciones.')
    tipo = models.ForeignKey(LC_DerechoTipo, on_delete=models.PROTECT, related_name='derechos',blank= False, null=False) 
    fraccion_derecho = models.DecimalField('Fracción de Derecho', max_digits=5, decimal_places=2, blank=False, null=False, help_text="Fracción del derecho en relacion a la tenencia y el área ocuapa (entre 0.00 y 1.00)")
    fecha_inicio_tenencia = models.DateField('Fecha de inicio de tenencia', auto_now=False, auto_now_add=False, blank=True, null=True,help_text='Feha en que comenzó la tenencia del derecho')

    class Meta:
        """Meta definition for LC_Derecho."""

        verbose_name = 'Derecho'
        verbose_name_plural = 'Derechos'

    def __str__(self):
        """Unicode representation of LC_Derecho."""
        return f"{self.tipo} - Fracción: {self.fraccion_derecho}"










