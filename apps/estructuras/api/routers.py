from rest_framework.routers import DefaultRouter

from apps.estructuras.api.views import ExtDireccionViewSet, ExtInteresadoViewSet, EstructuraNovedadNumeroPredialViewSet, NovedadFMIViewSet, ExtArchivoSerializerViewSet, AreaValorSerializerViewSet, VolumenValorSerializerViewSet

router = DefaultRouter()

router.register(r'ExtDireccion', ExtDireccionViewSet, basename = 'ExtDireccion')
router.register(r'ExtInteresado', ExtInteresadoViewSet, basename = 'ExtInteresado')
router.register(r'EstructuraNovedadNumeroPredial', EstructuraNovedadNumeroPredialViewSet, basename = 'EstructuraNovedadNumeroPredial')
router.register(r'NovedadFMI', NovedadFMIViewSet, basename = 'NovedadFMI')
router.register(r'ExtArchivo', ExtArchivoSerializerViewSet, basename = 'ExtArchivo')
router.register(r'AreaValor', AreaValorSerializerViewSet, basename = 'AreaValor')
router.register(r'VolumenValor', VolumenValorSerializerViewSet, basename = 'VolumenValor')

urlpatterns = router.urls