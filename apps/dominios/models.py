from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

# Create your models here.
class COL_UnidadAdministrativaBasicaTipo(BaseModel):
    """Model definition for COL_UnidadAdministrativaBasicaTipo."""

    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        PREDIO = 'Predio', 'Predio'
        ORDENAMIENTO_TERRITORIAL = 'Ordenamiento_Territorial', 'Ordenamiento Territorial'
        SERVICIOS_PUBLICOS = 'Servicios_Publicos', 'Servicios Públicos'
        RESERVAS_NATURALES = 'Reservas_Naturales', 'Reservas Naturales'
        PARQUES_NATURALES = 'Parques_Naturales', 'Parques Naturales'
        AMENAZAS_RIESGOS = 'Amenazas_Riesgos', 'Amenazas y Riesgos'
        SERVIDUMBRE = 'Servidumbre', 'Servidumbre'
        SUPERFICIES_AGUA = 'Superficies_Agua', 'Superficies de Agua'
        TRANSPORTE = 'Transporte'

    tipo = models.CharField(choices=Tipo.choices, max_length=50, verbose_name='Tipo de Unidad Administrativa Básica',  help_text='Tipo de unidad administrativa básica')

    class Meta:
        """Meta definition for COL_UnidadAdministrativaBasicaTipo."""

        verbose_name = 'Tipo de Unidad Administrativa Básica'
        verbose_name_plural = 'Tipos de Unidad Administrativa Básica'

    def __str__(self):
        """Unicode representation of COL_UnidadAdministrativaBasicaTipo."""
        return self.get_tipo_display()

class LC_PredioTipo(BaseModel):
    """Model definition for LC_PredioTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        PUBLICO_BALDIO = 'Publico_Baldio','Baldío (Público)'
        PUBLICO_FISCAL_PATRIMONIAL_='Publico_Fiscal_Patrimonial', 'Fiscal Patrimonial (Público)'
        PUBLICO_USO_PUBLICO ='Publico_Uso_Publico', 'Uso Público (Público)'
        PUBLICO_PUBLICO ='Publico', 'Público'
        PRIVADO ='Privado'

    tipo = models.CharField(choices=Tipo.choices, max_length=50, verbose_name='Tipo de Predio', help_text='Tipo de predio, puede ser público o privado con subcategorías para público')

    class Meta:
        """Meta definition for LC_PredioTipo."""

        verbose_name = 'Tipo de Predio'
        verbose_name_plural = 'Tipos de Predios'

    def __str__(self):
        """Unicode representation of LC_PredioTipo."""
        return self.get_tipo_display()
    
class LC_CondicionPredioTipo(BaseModel):
    """Model definition for LC_CondicionPredioTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for MODELNAME."""
    
        # TODO: Define fields here
        NPH = 'NPH', 'NPH'
        PH_MATRIZ = 'PH_Matriz', 'Matriz (PH)'
        PH_UNIDAD_PREDIAL = 'PH_Unidad_Predial', 'Unidad Predial (PH)'
        CONDOMINIO_MATRIZ = 'Condominio_Matriz', 'Matriz (Condominio)'
        CONDOMINIO_UNIDAD_PREDIAL = 'Condominio_Unidad_Predial', 'Unidad Predial (Condominio)'
        PARQUE_CEMENTERIO_MATRIZ = 'Parque_Cementerio_  Matriz', 'Matriz (Parque Cementerio)'
        PARQUE_CEMENTERIO_UNIDAD_PREDIAL = 'Parque_Cementerio_Unidad_Predial', 'Unidad Predial (Parque Cementerio)'
        VIA = 'Via', 'Vía'
        INFORMAL = 'Informal', 'Informal'
        BIEN_USO_PUBLICO = 'Bien_Uso_Publico', 'Bien de Uso Público'
    
    tipo = models.CharField(choices=Tipo, max_length=50, verbose_name='Tipo de Condición de Predio', help_text='Tipo de condición de predio, con varias subcategorias')

    class Meta:
        """Meta definition for LC_CondicionPredioTipo."""

        verbose_name = 'Condición de Predio'
        verbose_name_plural = 'Condiciones de Predios'

    def __str__(self):
        """Unicode representation of LC_CondicionPredioTipo."""
        return self.get_tipo_display()

class LC_DestinacionEconomicaTipo(BaseModel):
    """Model definition for LC_DestinacionEconomicaTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for MODELNAME."""
    
        # TODO: Define fields here
        ACUICOLA = 'Acuicola','Acuícola'
        AGRICOLA = 'Agricola','Agrícola'
        AGROINDUSTRIAL = 'Agroindustrial','Agroindustrial'
        AGROPECUARIO = 'Agropecuario','Agropecuario'
        AGROFORESTAL = 'Agroforestal','Agroforestal'
        COMERCIAL = 'Comercial','Comercial'
        CULTURAL = 'Cultural','Cultural'
        EDUCATIVO = 'Educativo','Educativo'
        FORESTAL = 'Forestal','Forestal'
        HABITACIONAL = 'Habitacional','Habitacional'
        INDUSTRIAL = 'Industrial','Industrial'
        INFRAESTRUCTURA_ASOCIADA_PRODUCCION_AGROPECUARIA = 'Infraestructura_Asociada_Produccion_Agropecuaria', 'Infraestructura Asociada a Producción Agropecuaria'
        INFRAESTRUCTURA_HIDRAULICA = 'Infraestructura_Hidraulica','Infraestructura Hidráulica'
        INFRAESTRUCTURA_SANEAMIENTO_BASICO = 'Infraestructura_Saneamiento_Basico','Infraestructura de Saneamiento Básico'
        INFRAESTRUCTURA_SEGURIDAD = 'Infraestructura_Seguridad','Infraestructura de Seguridad'
        INFRAESTRUCTURA_TRANSPORTE = 'Infraestructura_Transporte','Infraestructura de Transporte'
        INSTITUCIONAL = 'Institucional', 'Institucional'
        MINERIA_HIDROCARBUROS = 'Mineria_Hidrocarburos', 'Minería e Hidrocarburos'
        LOTE_URBANIZABLE_NO_URBANIZADO = 'Lote_Urbanizable_No_Urbanizado','Lote Urbanizable No Urbanizado'
        LOTE_URBANIZADO_NO_CONSTRUIDO = 'Lote_Urbanizable_No_Construido','Lote Urbanizable No Construido'
        LOTE_NO_URBANIZABLE = 'Lote_No_Urbanizable','Lote No Urbanizable'
        PECUARIO = 'Pecuario','Pecuario'
        RECREACIONAL = 'Recreacional','Recreacional'
        RELIGIOSO = 'Religioso','Religioso'
        SALUBRIDAD = 'Salubridad','Salubridad'
        SERVICIOS_FUNERARIOS = 'Servicios_Funerarios','Servicios Funerarios'
        USO_PUBLICO = 'Uso_Publico','Uso Público'

    tipo = models.CharField(choices=Tipo.choices, max_length=100, verbose_name='Tipo de Destinacón Económica', help_text='Tipo de destinación económica del predio')

    class Meta:
        """Meta definition for LC_DestinacionEconomicaTipo."""

        verbose_name = 'Tipo de Destinación Económica'
        verbose_name_plural = 'Tipos de Destinación Económica'

    def __str__(self):
        """Unicode representation of LC_DestinacionEconomicaTipo."""
        return self.get_tipo_display()

class TipoDireccionTipo(BaseModel):
    """Model definition for TipoDireccionTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        ESTRUCTURADA = 'Estructurada', 'Estructurada'
        NO_ESTRUCTURADA = 'No Estructurada', 'No Estructurada'
    
    tipo = models.CharField(choices=Tipo.choices, max_length=50, verbose_name='Tipo de dirección', help_text='Tipo de dirección')

    class Meta:
        """Meta definition for TipoDireccionTipo."""

        verbose_name = 'Tipo de Dirección'
        verbose_name_plural = 'Tipos de Direcciones'

    def __str__(self):
        """Unicode representation of TipoDireccionTipo."""
        return self.get_tipo_display()

class ClaseViaPrincipalClase(BaseModel):
    """Model definition for ClaseViaPincipalClase."""

    # TODO: Define fields here
    class Clase(models.TextChoices):
        """Model definition for Clase."""
    
        # TODO: Define fields here
        AVENIDA_CALLE = 'Avenida_Calle','Avenida Calle'
        AVENIDA_CARRERA = 'Avenida_Carrera','Avenida Carrera'
        AVENIDA = 'Avenida', 'Avenida'
        AUTOPISTA = 'Autopista', 'Autopista'
        CIRCUNVALAR = 'Circunvalar', 'Circunvalar'
        CALLE = 'Calle', 'Calle'
        CARRERA = 'Carrera','Carrera'
        DIAGONAL = 'Diagonal','Diagonal'
        TRANSVERSAL = 'Transversal','Transversal'
        CIRCULAR = 'Circular', 'Circular'

    clase = models.CharField(choices=Clase.choices, max_length=50,verbose_name='Clase de Vía Principal', help_text='Clase de vía principal')

    class Meta:
        """Meta definition for ClaseViaPincipalClase."""

        verbose_name = 'Clase de Vía Principal'
        verbose_name_plural = 'Clases de Vías Principales'

    def __str__(self):
        """Unicode representation of ClaseViaPincipalClase."""
        return self.get_clase_display()

class SectorTipo(BaseModel):
    """Model definition for Sector."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        NORTE = 'Norte', 'Norte'
        SUR = 'Sur', 'Sur'
        ESTE = 'Este','Este'
        OESTE = 'Oeste', 'Oeste'
    
    tipo = models.CharField(choices=Tipo.choices, max_length=10, verbose_name='Sector', help_text= 'Sector de la ciudad o del predio')
    
    class Meta:
        """Meta definition for Sector."""

        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'

    def __str__(self):
        """Unicode representation of Sector."""
        return self.get_tipo_display()

class LC_ResultadoVisitaTipo(BaseModel):
    """Model definition for LC_ResultadoVisitaTipo."""

    # TODO: Define fields here
    class Resultado(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        EXITOSO = 'Exitoso', 'Exitoso'
        INCOMPLETO = 'Incompleto', 'Incompleto'
        NO_HAY_NADIE = 'No_Hay_Nadie', 'No hay nadie'
        NO_PERMITIERON_ACCESO = 'No_Permitieron_Acceso', 'No permitieron acceso'
        MENOR_EDAD = 'Menor_Edad', 'Menor edad'
        SITUACION_ORDEN_PUBLICO = 'Situacion_Orden_Publico','Situación de orden público'
        ZONA_DIFICIL_ACCESO = 'Zona_Dificil_Acceso','Zona de dificil acceso'
        SIN_VISITA = 'Sin visita', 'Sin visita'

    resultado = models.CharField(choices=Resultado.choices, max_length=50, verbose_name='Resultado de visita', help_text='Resultado obtenido tras la visita predial')

    class Meta:
        """Meta definition for LC_ResultadoVisitaTipo."""

        verbose_name = 'Resultado de visita'
        verbose_name_plural = 'Resultados de visita'

    def __str__(self):
        """Unicode representation of LC_ResultadoVisitaTipo."""
        return self.get_resultado_display()

class TipoNovedadTipo(BaseModel):
    """Model definition for Tipo_Novedad."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Novedad."""
    
        # TODO: Define fields here
        ENGLOBE = 'Englobe', 'Englobe de predios'
        DESENGLOBE = 'Desenglobe', 'Desenglobe de predio'
        MODIFICACION = 'MOdificacion', 'Modificación del número predial'
        CORRECCION = 'Correccion', 'Correción de datos'

    tipo = models.CharField(choices=Tipo.choices, max_length=100, verbose_name='Tipo de novedad', help_text='Indica los diferentes tipos de modificaciones que puede tener el número predial')

    class Meta:
        """Meta definition for Tipo_Novedad."""

        verbose_name = 'Tipo de Novedad'
        verbose_name_plural = 'Tipos de Novedades'

    def __str__(self):
        """Unicode representation of Tipo_Novedad."""
        return self.get_tipo_display()
    
class TipoNovedadFMITipo(BaseModel):
    """Model definition for TipoNovedadFMITipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        FMI_NO_ENCONTRADO = 'FMI_No_Encontrado', 'FMI no encontrado'
        FMI_DUPLICADO = 'FMI Duplicado', 'FMI duplicado'
        FMI_INEXISTENTE = 'FMI_Inexistente', 'FMI Inexistente'
        FMI_INCORRECTO = 'FMI_Incorrecto', 'FMI Incorrecto'
        FMI_DESACTUALIZADO = 'FMI_Desactualizado', 'FMI Desactualizado'

    tipo = models.CharField(choices=Tipo.choices, max_length=100, verbose_name='Tipo de Novedad FMI', help_text='Indica las diferencias o inexactitudes relativas al registro de predios en el FMI')

    class Meta:
        """Meta definition for TipoNovedadFMITipo."""

        verbose_name = 'Tipo de Novedad FMI'
        verbose_name_plural = 'Tipos de Novedades FMI'

    def __str__(self):
        """Unicode representation of TipoNovedadFMITipo."""
        return self.get_tipo_display()
    
class CR_DocumentoTipo(BaseModel):
    """Model definition for CR_DocumentoTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for CR_DocumentoTipo."""
    
        # TODO: Define fields here
        CEDULA_CIUDADANIA = 'Cedula_Ciudadania', 'Cédula Ciudadanía'
        CEDULA_EXTRANJERIA = 'Cedula_Extranjeria', 'Cédula EXtranjería'
        NIT = 'NIT', 'NIT'
        TARJETA_IDENTIDAD = 'Tarjeta_Identidad', 'Tarjeta de Identidad'
        REGISTRO_CIVIL = 'Registro_Civil', 'Registro Civil'
        SECUENCIAL = 'Secuencial', 'Secuencial'
        PASAPORTE = 'Pasaporte', 'Pasaporte'

    tipo = models.CharField(choices=Tipo.choices, max_length=50, verbose_name='Tipo de Documento', help_text='Tipo de documento de identificación de la persona')

    class Meta:
        """Meta definition for CR_DocumentoTipo."""

        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'

    def __str__(self):
        """Unicode representation of CR_DocumentoTipo."""
        return self.get_tipo_display()

class LC_DerechoTipo(BaseModel):
    """Model definition for LC_DerechoTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        DOMINIO = 'Dominio'
        OCUPACION = 'Ocupación'
        POSESION = 'Posesión'
    tipo = models.CharField(choices=Tipo.choices, max_length=50, verbose_name='Tipo de Derecho', help_text='Tipo de derecho relacionado con la tenencia del predio')  

    class Meta:
        """Meta definition for LC_DerechoTipo."""

        verbose_name = 'Tipo de Derecho'
        verbose_name_plural = 'Tipos de Derechos'

    def __str__(self):
        """Unicode representation of LC_DerechoTipo."""
        return self.get_tipo_display()

class CR_InteresadoTipo(BaseModel):
    """Model definition for COL_InteresdoTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for MODELNAME."""
    
        # TODO: Define fields here
        PERSONA_NATURAL = 'Persona natural'
        PERSONA_JURIDICA = 'Persona juridica'
    tipo = models.CharField(choices=Tipo.choices, max_length=50, verbose_name='Tipo de interesado', help_text='Persona natural que actúa a nombre propio y persona jurica que actúa como institución')

    class Meta:
        """Meta definition for COL_InteresdoTipo."""

        verbose_name = 'Tipo de interesado'
        verbose_name_plural = 'Tipos de interesados'

    def __str__(self):
        """Unicode representation of COL_InteresdoTipo."""
        return self.get_tipo_display()
    
class CR_SexoTipo(BaseModel):
    """Model definition for CR_SexoTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        MASCULINO = 'Masculino'
        FEMENINO = 'Femenino'
        SIN_DETERMINAR = 'Sin determinar'

    tipo = models.CharField(choices=Tipo, max_length=50, verbose_name='Tipo de sexo', help_text='Corresponde a "Masculino" y "Femenino" según como aparezca en el tipo de documento de identidad')      

    class Meta:
        """Meta definition for CR_SexoTipo."""

        verbose_name = 'Tipo de sexo'
        verbose_name_plural = 'Tipos de sexo'

    def __str__(self):
        """Unicode representation of CR_SexoTipo."""
        return self.get_tipo_display()
    
class CR_GrupoEtnicoTipo(BaseModel):
    """Model definition for CR_GrupoEtnicoTIpo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        INDIGENA = 'Indígena'
        RROM = 'Rrom'
        RAIZAL = 'Raizal'
        PALENQUERO = 'Palenquero'
        NEGRO_AFROCOLOMBIANO = 'Negro o afrocolombiano'
        NINGUNO = 'Ninguno'
    
    tipo = models.CharField(choices=Tipo, max_length=50, verbose_name='Tipo de grupo étnico', help_text='Grupo de persona a la cual pertenece el interesado, quienes comparten una misma ideología cultural.')
    
    class Meta:
        """Meta definition for CR_GrupoEtnicoTIpo."""

        verbose_name = 'Tipo de grupo étnico'
        verbose_name_plural = 'Tipos de grupos étnicos'

    def __str__(self):
        """Unicode representation of CR_GrupoEtnicoTIpo."""
        return self.get_tipo_display()
    
class COL_GrupoInteresadoTipo(BaseModel):
    """Model definition for COL_GrupoInteresadoTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        GRUPO_CIVIL = 'Grupo civil'
        GRUPO_EMPRESARIAL = 'Grupo empresarial'
        GRUPO_ETNICO = 'Grupo étnico'
        GRUPO_MIXTO = 'Grupo mixto'

    tipo = models.CharField(choices=Tipo, max_length=50, verbose_name='Tipo de grupo de interesados')
    
    class Meta:
        """Meta definition for COL_GrupoInteresadoTipo."""

        verbose_name = 'Tipo de grupo de interesado'
        verbose_name_plural = 'Tipos de grupo de interesados'

    def __str__(self):
        """Unicode representation of COL_GrupoInteresadoTipo."""
        return self.get_tipo_display()
    
class COL_EstadoDisponibilidadTipo(BaseModel):
    """Model definition for COL_EstadoDisponibilidadTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        CONVERTIDO = 'Convertido', 'Convertido'
        DESCONOCIDO = 'Desconocido', 'Desconocido'
        DISPONIBLE = 'Disponible', 'Disponible'
    
    tipo = models.CharField(choices=Tipo, max_length=50, verbose_name='Tipos de estado de disponibilidad')

    class Meta:
        """Meta definition for COL_EstadoDisponibilidadTipo."""

        verbose_name = 'Tipo de estado de disponibilidad'
        verbose_name_plural = 'Tipos de estados de disponibiidad'

    def __str__(self):
        """Unicode representation of COL_EstadoDisponibilidadTipo."""
        return self.get_tipo_display()
    
class CI_Forma_Presentacion_Codigo(BaseModel):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    class Codigo(models.TextChoices):
        """Model definition for MODELNAME."""
    
        # TODO: Define fields here
        IMAGEN = 'Imagen', 'Imagen'
        DOCUMENTO = 'Documento', 'Documento'
        MAPA = 'Mapa', 'Mapa'
        VIDEO = 'Video', 'Video'

    codigo = models.CharField(choices=Codigo, max_length=50, verbose_name='Tipos de formatos de presentación de la fuente')

    class Meta:
        """Meta definition for CI_Forma_Presentacion_Codigo."""

        verbose_name = 'Tipo de formato'
        verbose_name_plural = 'Tipos de formatos'

    def __str__(self):
        """Unicode representation of CI_Forma_Presentacion_Codigo."""
        return self.get_codigo_display()

class COL_FuenteAdministrativaTipo(BaseModel):
    """Model definition for COL_FuenteAdministrativaTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        DOCUMENTO_PUBLICO = 'Documento_publico', 'Documento Público'
        DOCUMENTO_PRIVADO = 'Documento_privado', 'Documento Privado'

    tipo = models.CharField(choices=Tipo, max_length=50, verbose_name='Tipo de documento.')

    class Meta:
        """Meta definition for COL_FuenteAdministrativaTipo."""

        verbose_name = 'Tipo de fuente administrativa (COL)'
        verbose_name_plural = 'Tipos de fuentes administrativas (COL)'

    def __str__(self):
        """Unicode representation of COL_FuenteAdministrativaTipo."""
        return self.get_tipo_display()
    
class LC_FuenteAdministrativaTipo(BaseModel):
    """Model definition for LC_FuenteAdministrativaTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        DOCUMENTO_PRIVADO = 'Documento_Privado','Documento privado'
        ESCRITURA_PUBLICA = 'Escritura_Publica','Escritura pública (Documento público)'
        SENTENCIA_JUDICIAL = 'Sentencia_Judicial','Sentencia judicial (Documento público)'
        ACTO_ADMINISTRATIVO = 'Acto_Administrativo','Acto administrativo (Documento público)'
        SIN_DOCUMENTO = 'Sin_Documento','Sin documento'

    tipo = models.CharField(choices=Tipo, max_length=100, verbose_name='Tipos de documentos.')

    class Meta:
        """Meta definition for LC_FuenteAdministrativaTipo."""

        verbose_name = 'Tipo de fuente administrativa (LC)'
        verbose_name_plural = 'Tipos de fuentes administrativas (LC)'

    def __str__(self):
        """Unicode representation of LC_FuenteAdministrativaTipo."""
        return self.get_tipo_display()
    
class COL_FuenteEspacialTipo(BaseModel):
    """Model definition for COL_FuenteEspacialTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        CROQUIS_CAMPO = 'Croquis_Campo','Croquis de campo'
        DATOS_CRUDOS = 'Datos_Crudos','Datos crudos(GPS, Estación total, LIDAR)'
        ORTOFOTO = 'Ortofoto','Ortofoto'
        INFORME_TECNICO = 'Informe_Tecnico','Informe técnico'
        REGISTRO_FOTOGRAFICO = 'Registro_Fotografico','Registro fotográfico'

    tipo = models.CharField(choices=Tipo, max_length=100, verbose_name='Tipos de fuente espacial')

    class Meta:
        """Meta definition for COL_FuenteEspacialTipo."""

        verbose_name = 'Tipo de fuente espacial'
        verbose_name_plural = 'Tipos de fuentes espaciales'

    def __str__(self):
        """Unicode representation of COL_FuenteEspacialTipo."""
        return self.get_tipo_display()

class COL_AreaTipo(BaseModel):
    """Model definition for COL_AreaTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        AREA_CATASTRAL_GRAFICA = 'Area_catastral_grafica','Àrea catastral gráfica del predio'
        AREA_CATASTRAL_ALFANUMERICA = 'Area_catastral_alfanumerica','Área catastral alfanumérica'
    
    tipo = models.CharField(choices=Tipo, max_length=50, verbose_name='Tipos de área catastral')

    class Meta:
        """Meta definition for COL_AreaTipo."""

        verbose_name = 'Tipo de área'
        verbose_name_plural = 'Tipos de área'

    def __str__(self):
        """Unicode representation of COL_AreaTipo."""
        return self.get_tipo_display()
    
class COL_DimensionTipo(BaseModel):
    """Model definition for COL_DimensionTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        DIM2D = 'Dim2D', 'Dimensión 2D'
        DIM3D = 'Dim3D', 'Dimensión 3D'
        OTRO = 'Otro', 'Otra dimensiòn'

    tipo = models.CharField(choices=Tipo, max_length=50, verbose_name='Tipos de dimensiones')

    class Meta:
        """Meta definition for COL_DimensionTipo."""

        verbose_name = 'Tipo de dimensión'
        verbose_name_plural = 'Tipos de dimensiones'

    def __str__(self):
        """Unicode representation of COL_DimensionTipo."""
        return self.get_tipo_display()
    
class COL_RelacionSuperficieTipo(BaseModel):
    """Model definition for COL_RelacionSuperficieTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        EN_RASANTE = 'En_Rasante','En rasante'
        EN_VUELO = 'En_Vuelo','En vuelo'
        EN_SUBSUELO = 'En_subsuelo','En subsuelo'
        OTRO = 'Otro','Otro'

    tipo = models.CharField(choices=Tipo, max_length=50, verbose_name='Tipos de superficie')

    class Meta:
        """Meta definition for COL_RelacionSuperficieTipo."""

        verbose_name = 'Tipo de relación de superficie'
        verbose_name_plural = 'Tipos de relación de superficie'

    def __str__(self):
        """Unicode representation of COL_RelacionSuperficieTipo."""
        return self.get_tipo_display()
    
class COL_VolumenTipo(BaseModel):
    """Model definition for COL_VolumenTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        OFICIAL = 'Oficial', 'Oficial'
        CALCULADO = 'Calculado', 'Calculado'
        OTRO = 'Otro', 'Otro'

    tipo = models.CharField(choices=Tipo, max_length=50, verbose_name='Tipos de volumen')    

    class Meta:
        """Meta definition for COL_RelacionSuperficieTipo."""

        verbose_name = 'Tipo de volumen'
        verbose_name_plural = 'Tipos de volumen'

    def __str__(self):
        """Unicode representation of COL_VolumenTipo."""
        return self.get_tipo_display()
    
class CR_ConstruccionPlantaTipo(BaseModel):
    """Model definition for CR_."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for MODELNAME."""
    
        # TODO: Define fields here
        PISO = 'Piso', 'Piso'
        MEZANINE = 'Mezanine', 'Mezanine'
        SOTANO = 'Sotano','Sótano'
        SEMISOTANO = 'Semisotano', 'Semisótano'
        SUBTERRANEO = 'Subterraneo','Subterraneo'

    tipo = models.CharField(choices=Tipo, max_length=50, verbose_name='Tipos de plantas.')

    class Meta:
        """Meta definition for CR_."""

        verbose_name = 'Tipo de planta de construcción'
        verbose_name_plural = 'Tipos de plantas de construcción'

    def __str__(self):
        """Unicode representation of CR_."""
        return self.get_tipo_display()
    
class CR_UnidadConstruccionTipo(BaseModel):
    """Model definition for CR_UnidadConstruccionTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        RESIDENCIAL = 'Residencial', 'Residencial'
        COMERCIAL = 'Comercial', 'Comercial'
        INDUSTRIAL = 'Industrial', 'Industrial'
        INSTITUCIONAL = 'Institucional', 'Institucional'
        ANEXO = 'Anexo', 'Anexo'

    tipo = models.CharField(choices=Tipo, max_length=50, verbose_name='Tipos de unidad de construcción')    

    class Meta:
        """Meta definition for CR_UnidadConstruccionTipo."""

        verbose_name = 'Tipo de unidad de construcción'
        verbose_name_plural = 'Tipos de unidad de construcción'

    def __str__(self):
        """Unicode representation of CR_UnidadConstruccionTipo."""
        return self.get_tipo_display()

class CR_UsoUConsTipo(BaseModel):
    """Model definition for CR_UsoUConsTipo."""

    # TODO: Define fields here
    class Tipo(models.TextChoices):
        """Model definition for Tipo."""
    
        # TODO: Define fields here
        APARTAMENTOS_4_Y_MAS_PISOS_EN_PH = 'Apartamentos_4_y_mas_pisos_en_PH', 'Apartamentos más de 4 pisos en PH (Residencial)'
        APARTAMENTOS_4_Y_MAS_PISOS = 'Apartamentos_4_y_mas_pisos', 'Apartamentos de 4 y más pisos (Residencial)'
        BARRACAS = 'Barracas', 'Barracas (Residencial)'
        CASA_ELBAS = 'Casa_Elbas', 'Casa Elbas (Residencial)'
        DEPOSITOS_LOCKERS = 'Depositos_Lockers', 'Depósitos o lockers (Residencial)'
        GARAJES_CUBIERTOS = 'Garajes_Cubiertos', 'Garajes cubiertos (Residencial)'
        GARAJES_EN_PH = 'Garajes_En_PH', 'Garajes en PH (Residencial)'
        SALON_COMUNAL = 'Salon_Comunal', 'Salón comunal (Residencial)'
        SECADERO_ROPA = 'Secadero_Ropa', 'Secadero de ropa (Residencial)'
        VIVIENDA_COLONIAL = 'Vivienda_Colonial', 'Vivienda colonial (Residencial)'
        VIVIENDA_COLONIAL_EN_PH = 'Vivienda_Colonial_en_PH', 'Vivienda colonial en PH (Residencial)'
        VIVIENDA_HASTA_3_PISOS = 'Vivienda_Hasta_3_Pisos', 'Vivienda hasta 3 pisos (Residencial)'
        VIVIENDA_HASTA_3_PISOS_EN_PH = 'Vivienda_Hasta_3_Pisos_En_PH', 'Vivienda hasta 3 pisos en PH (Residencial)'
        VIVIENDA_RECREACIONAL = 'Vivienda_Recreacional', 'Vivienda recreacional (Residencial)'
        VIVIENDA_RECREACIONAL_EN_PH = 'Vivienda_Recreacional_En_PH', 'Vivienda recreacional en PH (Residencial)'
        BODEGAS_COMERCIALES_GRANDES_ALMACENES = 'Bodegas_Comerciales_Grandes_Almacenes', 'Bodegas comerciales - Grandes almacenes (Comercial)'
        BODEGAS_COMERCIALES_EN_PH = 'Bodegas_Comerciales_en_PH', 'Bodegas Comerciales en PH (Comercial)'
        CENTROS_COMERCIALES = 'Centros_Comerciales', 'Centros comerciales (Comercial)'
        CENTROS_COMERCIALES_EN_PH = 'Centros_Comerciales_en_PH', 'Centros comerciales en PH (Comercial)'
        CLUBES_CASINOS = 'Clubes_Casinos', 'Clubes - Casinos (Comercial)'
        COMERCIO = 'Comercio', 'Comercio (Comercial)'
        COMERCIO_COLONIAL = 'Comercio_Colonial', 'Comercio colonial (Comercial)'
        COMERCIO_EN_PH = 'Comercio_en_PH', 'Comercio en PH (Comercial)'
        HOTEL_COLONIAL = 'Hotel_Colonial', 'Hotel colonial (Comercial)'
        HOTELES = 'Hoteles', 'Hoteles (Comercial)'
        HOTELES_EN_PH = 'Hoteles_en_PH', 'Hoteles en PH (Comercial)'
        OFICINAS_CONSULTORIOS = 'Oficinas_Consultorios', 'Oficinas - Consultorios (Comercial)'
        OFICINAS_CONSULTORIOS_COLONIALES = 'Oficinas_Consultorios_Coloniales', 'Oficinas - Consultorios coloniales (Comercial)'
        OFICINAS_CONSULTORIOS_EN_PH = 'Oficinas_Consultorios_en_PH', 'Oficinas Consultorios en PH (Comercial)'
        PARQUE_DIVERSIONES = 'Parque_Diversiones', 'Parque de diversiones (Comercial)'
        PARQUEADEROS = 'Parqueaderos', 'Parqueaderos (Comercial)'
        PARQUEADEROS_EN_PH = 'Parqueaderos_en_PH', 'Parqueaderos en PH (Comercial)'
        PENSIONES_Y_RESIDENCIAS = 'Pensiones_y_Residencias', 'Pensiones y residencias (Comercial)'
        PLAZA_MERCADO = 'Plaza_Mercado', 'Plaza de mercado (Comercial)'
        RESTAURANTE_COLONIAL = 'Restaurante_Colonial', 'Restaurante colonial (Comercial)'
        RESTAURANTES = 'Restaurantes', 'Restaurantes (Comercial)'
        RESTAURANTES_EN_PH = 'Restaurantes_en_PH', 'Restaurantes en PH (Comercial)'
        TEATRO_CINEMAS = 'Teatro_Cinemas', 'Teatro - Cinemas (Comercial)'
        TEATRO_CINEMAS_EN_PH = 'Teatro_Cinemas_en_PH', 'Teatro - Cinemas en PH (Comercial)'
        BODEGA_CASA_BOMBA = 'Bodega_Casa_Bomba', 'Bodega casa bomba (Industrial)'
        BODEGAS_CASA_BOMBA_EN_PH = 'Bodegas_Casa_Bomba_en_PH', 'Bodegas casa bomba en PH (Industrial)'
        INDUSTRIAS = 'Industrias', 'Industrias (Industrial)'
        INDUSTRIAS_EN_PH = 'Industrias_en_PH', 'Industrias en PH (Industrial)'
        TALLERES = 'Talleres', 'Talleres (Industrial)'
        AULAS_DE_CLASES = 'Aulas_de_Clases', 'Aulas de clases (Institucional)'
        BIBLIOTECA = 'Biblioteca', 'Biblioteca (Institucional)'
        CARCELES = 'Carceles', 'Cárceles (Institucional)'
        CASAS_DE_CULTO = 'Casas_de_Culto', 'Casas de culto (Institucional)'
        CLINICAS_HOSPITALES_CENTROS_MEDICOS = 'Clinicas_Hospitales_Centros_Medicos', 'Clínicas, hospitales, centros medicos (Institucional)'
        COLEGIO_Y_UNIVERSIDADES = 'Colegio_y_Universidades', 'Colegio y universidades (Institucional)'
        COLISEOS = 'Coliseos', 'Coliseos (Institucional)'
        ENTIDAD_EDUCATIVA_COLONIAL_COLEGIO_COLONIAL = 'Entidad_Educativa_Colonial_Colegio_Colonial', 'Entidad educativa colonial colegio colonial (Institucional)'
        ESTADIOS = 'Estadios', 'Estadios (Institucional)'
        FUERTES_Y_CASTILLOS = 'Fuertes_y_Castillos', 'Fuertes y Castillos (Institucional)'
        IGLESIA = 'Iglesia', 'Iglesia (Institucional)'
        IGLESIA_EN_PH = 'Iglesia_en_PH', 'Iglesia en PH (Institucional)'
        INSTALACIONES_MILITARES = 'Instalaciones_Militares', 'Instalaciones militares (Institucional)'
        JARDIN_INFANTIL_EN_CASA = 'Jardin_Infantil_en_Casa', 'Jardín infantil en casa (Institucional)'
        PARQUE_CEMENTERIO = 'Parque_Cementerio', 'Parque Cementerio (Institucional)'
        PLANETARIO = 'Planetario', 'Planetario (Institucional)'
        PLAZA_DE_TOROS = 'Plaza_de_Toros', 'Plaza de toros (Institucional)'
        PUESTOS_DE_SALUD = 'Puestos_de_Salud', 'Puestos de salud (Institucional)'
        MUSEOS = 'Museos', 'Museos (Institucional)'
        SEMINARIOS_CONVENTOS = 'Seminarios_Conventos', 'Seminarios, conventos (Institucional)'
        TEATRO = 'Teatro', 'Teatro (Institucional)'
        UNIDAD_DEPORTIVA = 'Unidad_Deportiva', 'Unidad deportiva (Institucional)'
        VELODROMO_PATINODROMO = 'Velodromo_Patinodromo', 'Velódromo, patinódromo (Institucional)'
        ALBERCAS_BANADERAS = 'Albercas_Banaderas', 'Albercas - Banaderas (Anexo)'
        BENEFICIADEROS = 'Beneficiaderos', 'Beneficiaderos (Anexo)'
        CAMARONERAS = 'Camaroneras', 'Camaroneras (Anexo)'
        CANCHAS = 'Canchas', 'Canchas (Anexo)'
        CANCHAS_DE_TENIS = 'Canchas_de_Tenis', 'Canchas de tenis (Anexo)'
        CARRETERA = 'Carretera', 'Carretera (Anexo)'
        CERRAMIENTO = 'Cerramiento', 'Cerramiento (Anexo)'
        CIMIENTOS_ESTRUCTURA_MUROS_Y_PLACA_BASE = 'Cimientos_Estructura_Muros_y_Placa_Base', 'Cimientos, estructura, muros y placa base (Anexo)'
        COCHERAS_MARRANERAS_PORQUERIZAS = 'Cocheras_Marraneras_Porquerizas', 'Cocheras - Marraneras - Porquerizas (Anexo)'
        CONSTRUCCION_EN_MEMBRANA_ARQUITECTONICA = 'Construccion_en_Membrana_Arquitectonica', 'Construcción en membrana arquitectónica (Anexo)'
        CONTENEDOR = 'Contenedor', 'Contenedor (Anexo)'
        CORRALES = 'Corrales', 'Corrales (Anexo)'
        ESTABLOS_PESEBRERAS_CABALLERIZAS = 'Establos_Pesebreras_Caballerizas', 'Establos - Pesebreras - Caballerizas (Anexo)'
        ESTACION_BOMBEO = 'Estacion_Bombeo', 'Estacion de bombeo (Anexo)'
        ESTACION_SISTEMA_TRANSPORTE = 'Estacion_Sistema_Transporte', 'Estacion de sistema de transporte (Anexo)'
        GALPONES_GALLINEROS = 'Galpones_Gallineros', 'Galpones - Gallineros (Anexo)'
        GLAMPING = 'Glamping', 'Glamping (Anexo)'
        HANGAR = 'Hangar', 'Hangar (Anexo)'
        KIOSCOS = 'Kioscos', 'Kioscos (Anexo)'
        LAGUNAS_DE_OXIDACION = 'Lagunas_de_Oxidacion', 'Lagunas de oxidacion (Anexo)'
        MARQUESINAS_PATIOS_CUBIERTOS = 'Marquesinas_Patios_Cubiertos', 'Marquesinas - Patios cubiertos (Anexo)'
        MUELLES = 'Muelles', 'Muelles (Anexo)'
        MURALLAS = 'Murallas', 'Murallas (Anexo)'
        PERGOLAS = 'Pergolas', 'Pérgolas (Anexo)'
        PISCINAS = 'Piscinas', 'Piscinas (Anexo)'
        PISTA_AEROPUERTO = 'Pista_Aeropuerto', 'Pista aeropuerto (Anexo)'
        POZOS = 'Pozos', 'Pozos (Anexo)'
        RAMADAS_COBERTIZOS_CANEYES = 'Ramadas_Cobertizos_Caneyes', 'Ramadas - Cobertizos - Caneyes (Anexo)'
        SECADEROS = 'Secaderos', 'Secaderos (Anexo)'
        SILOS = 'Silos', 'Silos (Anexo)'
        TANQUES = 'Tanques', 'Tanques (Anexo)'
        TOBOGANES = 'Toboganes', 'Toboganes (Anexo)'
        TORRE_DE_CONTROL = 'Torre_de_Control', 'Torre de control (Anexo)'
        TORRES_DE_ENFRIAMIENTO = 'Torres_de_Enfriamiento', 'Torres de enfriamiento (Anexo)'
        VIA_FERREA = 'Via_Ferrea', 'Vía Férrea (Anexo)'
        
    tipo = models.CharField(choices=Tipo, max_length=50, verbose_name='Tipos de uso de unidad de constrocción')

    class Meta:
        """Meta definition for CR_UsoUConsTipo."""

        verbose_name = 'Tipo de uso de unidad de construcción'
        verbose_name_plural = 'Tipos de usos de unidades de construcción'

    def __str__(self):
        """Unicode representation of CR_UsoUConsTipo."""
        return self.get_tipo_display()
    
class GeometriaClase(BaseModel):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    class Clase(models.TextChoices):
        """Model definition for TIpo."""
    
        # TODO: Define fields here
        TERRENO = 'Terreno', 'Terreno'
        CONSTRUCCION = 'Construccion', 'Construcción'
        UNIDAD_CONSTRUCCION = 'Unidad_Construcción', 'Unidad de construcción'

    clase = models.CharField(choices=Clase, max_length=50, verbose_name='Clases a la que pertenece la geometría.')
    
    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Clase de geometría'
        verbose_name_plural = 'Clases de geometrias'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.get_clase_display()




def cargar_datos_iniciales():
    """Carga automáticamente los valores iniciales para los modelos de dominio."""

    # Cargar valores en COL_UnidadAdministrativaBasicaTipo
    for valor, descripcion in COL_UnidadAdministrativaBasicaTipo.Tipo.choices:
        COL_UnidadAdministrativaBasicaTipo.objects.get_or_create(tipo=valor)

    # Cargar valores en LC_PredioTipo
    for valor, descripcion in LC_PredioTipo.Tipo.choices:
        LC_PredioTipo.objects.get_or_create(tipo=valor)

    # Cargar valores en LC_CondicionPredioTipo
    for valor, descripcion in LC_CondicionPredioTipo.Tipo.choices:
        LC_CondicionPredioTipo.objects.get_or_create(tipo=valor)

    # Cargar valores en LC_DestinacionEconomicaTipo
    for valor, descripcion in LC_DestinacionEconomicaTipo.Tipo.choices:
        LC_DestinacionEconomicaTipo.objects.get_or_create(tipo=valor)

    # Cargar valores en TipoDireccionTipo
    for valor, descripcion in TipoDireccionTipo.Tipo.choices:
        TipoDireccionTipo.objects.get_or_create(tipo=valor)

    # Cargar valores en ClaseViaPrincipalClase
    for valor, descripcion in ClaseViaPrincipalClase.Clase.choices:
        ClaseViaPrincipalClase.objects.get_or_create(clase=valor)

    # Cargar valores en SectorTipo
    for valor, descripcion in SectorTipo.Tipo.choices:
        SectorTipo.objects.get_or_create(tipo=valor)

    # Cargar valores en LC_ResultadoVisitaTipo
    for valor, descripcion in LC_ResultadoVisitaTipo.Resultado.choices:
        LC_ResultadoVisitaTipo.objects.get_or_create(resultado=valor)

    # Cargar valores en TipoNovedadTipo
    for valor, descripcion in TipoNovedadTipo.Tipo.choices:
        TipoNovedadTipo.objects.get_or_create(tipo=valor)

    # Cargar valores en TipoNovedadFMITipo
    for valor, descripcion in TipoNovedadFMITipo.Tipo.choices:
        TipoNovedadFMITipo.objects.get_or_create(tipo=valor)

    # Cargar valores en CR_DocumentoTipo
    for valor, descripcion in CR_DocumentoTipo.Tipo.choices:
        CR_DocumentoTipo.objects.get_or_create(tipo=valor)

    # Cargar valores en LC_DerechoTipo
    for valor, descripcion in LC_DerechoTipo.Tipo.choices:
        LC_DerechoTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in CR_InteresadoTipo.Tipo.choices:
        CR_InteresadoTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in CR_SexoTipo.Tipo.choices:
        CR_SexoTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in CR_GrupoEtnicoTipo.Tipo.choices:
        CR_GrupoEtnicoTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in COL_GrupoInteresadoTipo.Tipo.choices:
        COL_GrupoInteresadoTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in COL_EstadoDisponibilidadTipo.Tipo.choices:
        COL_EstadoDisponibilidadTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in CI_Forma_Presentacion_Codigo.Codigo.choices:
        CI_Forma_Presentacion_Codigo.objects.get_or_create(codigo=valor)

    for valor, descripcion in COL_FuenteAdministrativaTipo.Tipo.choices:
        COL_FuenteAdministrativaTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in LC_FuenteAdministrativaTipo.Tipo.choices:
        LC_FuenteAdministrativaTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in COL_FuenteEspacialTipo.Tipo.choices:
        COL_FuenteEspacialTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in COL_AreaTipo.Tipo.choices:
        COL_AreaTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in COL_DimensionTipo.Tipo.choices:
        COL_DimensionTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in COL_RelacionSuperficieTipo.Tipo.choices:
        COL_RelacionSuperficieTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in COL_VolumenTipo.Tipo.choices:
        COL_VolumenTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in CR_ConstruccionPlantaTipo.Tipo.choices:
        CR_ConstruccionPlantaTipo.objects.get_or_create(tipo=valor)
        
    for valor, descripcion in CR_UnidadConstruccionTipo.Tipo.choices:
        CR_UnidadConstruccionTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in CR_UsoUConsTipo.Tipo.choices:
        CR_UsoUConsTipo.objects.get_or_create(tipo=valor)

    for valor, descripcion in GeometriaClase.Clase.choices:
        GeometriaClase.objects.get_or_create(clase=valor)