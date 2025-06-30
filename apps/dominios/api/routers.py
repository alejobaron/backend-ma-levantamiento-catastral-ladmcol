from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.dominios.api.views import COL_UnidadAdministrativaBasicaTipoViewSet, LC_PredioTipoViewSet, LC_CondicionPredioTipoViewSet, LC_DestinacionEconomicaViewSet, LC_ResultadoVisitaViewSet, CR_DocumentoTipoViewSet, LC_DerechoTipoViewSet, CR_InteresadoTipoViewSet, CR_SexoTipoViewSet, CR_GrupoEtnicoTipoViewSet,COL_GrupoInteresadoTipoViewSet, COL_EstadoDisponibilidadTipoViewSet, CI_Forma_Presentacion_CodigoViewSet, COL_FuenteAdministrativaTipoViewSet, LC_FuenteAdministrativaTipoViewSet, COL_FuenteEspacialTipoViewSet, COL_DimensionTipoViewSet, COL_RelacionSuperficieTipoViewSet, CR_UnidadConstruccionTipoViewSet, CR_UsoUConsTipoViewSet, CR_ConstruccionPlantaTipoViewSet

router = DefaultRouter()
router.register(r'UnidadAdministrativaBasicaTipo', COL_UnidadAdministrativaBasicaTipoViewSet, basename='uab-tipos')
router.register(r'PredioTipo', LC_PredioTipoViewSet, basename='predio-tipos')
router.register(r'CondicionPredioTipo', LC_CondicionPredioTipoViewSet, basename='condicionpredio-tipos')
router.register(r'DestinacionEconomicaTipo', LC_DestinacionEconomicaViewSet, basename='destinacioneconomica-tipos')
router.register(r'ResultadoVisitaTipo', LC_ResultadoVisitaViewSet, basename='resultadovisita-tipos')
router.register(r'DocumentoTipo', CR_DocumentoTipoViewSet, basename='documento-tipos')
router.register(r'DerechoTipo', LC_DerechoTipoViewSet, basename='derecho-tipos')
router.register(r'InteresadoTipo', CR_InteresadoTipoViewSet, basename='interesado-tipos')
router.register(r'SexoTipo', CR_SexoTipoViewSet, basename='sexo-tipos')
router.register(r'GrupoEtnicoTipo', CR_GrupoEtnicoTipoViewSet, basename='grupoetnico-tipos')
router.register(r'GrupoInteresadoTipo', COL_GrupoInteresadoTipoViewSet, basename='grupointeresado-tipos')
router.register(r'EstadoDisponibilidadTipo', COL_EstadoDisponibilidadTipoViewSet, basename='estadodisponibilidad-tipos')
router.register(r'FormaPresentacionCodigo', CI_Forma_Presentacion_CodigoViewSet, basename='formapresentacioncodigo')
router.register(r'FuenteAdministrativaTipo', COL_FuenteAdministrativaTipoViewSet, basename='fuenteadministrativa-tipos')
router.register(r'FuenteAdministrativaTipoLC', LC_FuenteAdministrativaTipoViewSet, basename='fuenteadministrativalc-tipos')
router.register(r'FuenteEspacialTipo', COL_FuenteEspacialTipoViewSet, basename='fuenteespacial-tipos')
router.register(r'DimensionTipo', COL_DimensionTipoViewSet, basename='dimension-tipos')
router.register(r'RelacionSuperficieTipo', COL_RelacionSuperficieTipoViewSet, basename='relacionsuperficie-tipos')
router.register(r'UnidadConstruccionTipo', CR_UnidadConstruccionTipoViewSet, basename='unidadconstruccion-tipos')
router.register(r'UsoUnidadConstruccionTipo', CR_UsoUConsTipoViewSet, basename='usounidadconstruccion-tipos')
router.register(r'ConstruccionPlantaTipo', CR_ConstruccionPlantaTipoViewSet, basename='construccionplanta-tipos')

urlpatterns = [
    path('', include(router.urls)),
]


