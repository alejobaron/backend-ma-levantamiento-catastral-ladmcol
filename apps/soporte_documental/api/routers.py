from rest_framework.routers import DefaultRouter

from apps.soporte_documental.api.views import COL_FuenteViewSet, COL_FuenteAdministrativaViewSet, LC_FuenteAdministrativaViewSet, COL_FuenteEspacialViewSet, CR_FuenteEspacialViewSet

router = DefaultRouter()

router.register(r'COLFuente',COL_FuenteViewSet, basename = 'COLFuente')
router.register(r'COLFuenteAdministrativa', COL_FuenteAdministrativaViewSet, basename = 'COLFuenteAdministrativa')
router.register(r'LCFuenteAdministrativa', LC_FuenteAdministrativaViewSet, basename = 'LCFuenteAdministrativa')
router.register(r'COLFuenteEspacial', COL_FuenteEspacialViewSet, basename = 'COLFuenteEspacial')
router.register(r'CRFuenteEspacial', CR_FuenteEspacialViewSet, basename = 'CRFuenteEspacial')

urlpatterns = router.urls