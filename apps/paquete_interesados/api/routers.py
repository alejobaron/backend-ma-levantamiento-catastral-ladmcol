from rest_framework.routers import DefaultRouter

from apps.paquete_interesados.api.views import COL_InteresadoViewSet, CR_InteresadoViewSet, COL_AgrupacionInteresadosViewSet, col_miembrosViewSet, CR_AgrupacionInteresadosViewSet, LC_InteresadoContactoViewSet

router = DefaultRouter()

router.register(r'COLInteresado', COL_InteresadoViewSet, basename = 'COLInteresado')
router.register(r'CRInteresado', CR_InteresadoViewSet, basename = 'CRInteresado')
router.register(r'COLAgrupacionInteresados', COL_AgrupacionInteresadosViewSet, basename = 'COLAgrupacionInteresados')
router.register(r'Miembros', col_miembrosViewSet, basename = 'Miembros')
router.register(r'CRAgrupacionInteresados', CR_AgrupacionInteresadosViewSet, basename = 'CRAgrupacionInteresados')
router.register(r'InteresadoContacto', LC_InteresadoContactoViewSet, basename = 'InteresadoContacto')

urlpatterns = router.urls