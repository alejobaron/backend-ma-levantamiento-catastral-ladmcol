from rest_framework.routers import DefaultRouter
from apps.paquete_unidad_espacial.api.views import COL_UnidadEspacialViewSet, CR_ConstruccionViewSet, CR_CaracteristicasUnidadConstruccionViewSet, CR_UnidadConstruccionViewSet, CR_TerrenoViewSet

router = DefaultRouter()

router.register(r'UnidadEspacial', COL_UnidadEspacialViewSet, basename = 'UnidadEspacial')
router.register(r'Construccion', CR_ConstruccionViewSet, basename = 'Construccion')
router.register(r'CaracteristicasUnidadConstruccion', CR_CaracteristicasUnidadConstruccionViewSet, basename = 'CaracteristicasUnidadConstruccion')
router.register(r'UnidadConstruccion', CR_UnidadConstruccionViewSet, basename = 'UnidadConstruccion')
router.register(r'Terreno', CR_TerrenoViewSet, basename = 'Terreno')

urlpatterns = router.urls