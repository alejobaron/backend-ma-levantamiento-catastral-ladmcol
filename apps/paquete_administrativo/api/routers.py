from rest_framework.routers import DefaultRouter
from apps.paquete_administrativo.api.views import COL_UnidadAdministrativaBasicaViewSet, LC_PredioViewSet, cr_predio_copropiedadViewSet, CR_DatosPHCondominioViewSet, LC_DatosAdicionalesLevantamientoCatastralViewSet, LC_ContactoVisitaViewSet, COL_DRRViewSet, LC_DerechoViewSet

router = DefaultRouter()

router.register(r'UnidadAdministrativaBasica', COL_UnidadAdministrativaBasicaViewSet, basename ='UnidadAdministrtaivaBasica')
router.register(r'Predio', LC_PredioViewSet, basename ='Predio')
router.register(r'Predio_copropiedad', cr_predio_copropiedadViewSet, basename = 'Predio_copropiedad')
router.register(r'DatosPHCondominio', CR_DatosPHCondominioViewSet, basename = 'DatosPHCondominio')
router.register(r'DatosAdicionalesLevantamientoCatastral', LC_DatosAdicionalesLevantamientoCatastralViewSet, basename = 'DatosAdicionalesLevantamientoCatastral')
router.register(r'ContactoVisita', LC_ContactoVisitaViewSet, basename = 'ContactoVisita')
router.register(r'DRR', COL_DRRViewSet, basename = 'DRR')
router.register(r'Derecho', LC_DerechoViewSet, basename = 'Derecho')

urlpatterns = router.urls