from django.urls import path
from apps.paquete_administrativo.api.views import cr_predio_copropiedadListCreateAPIView, CR_DatosPHCondominioListCreateAPIView, LC_DatosAdicionalesLevantamientoCatastralListCreateAPIView, LC_ContactoVisitaListCreateAPIView, COL_DRRListCreateAPIView, LC_DerechoListCreateAPIView
from apps.paquete_administrativo.api.views import   cr_predio_copropiedadRetrieveUpdateDestroyAPIView, CR_DatosPHCondominioRetrieveUpdateDestroyAPIView, LC_DatosAdicionalesLevantamientoCatastralRetrieveUpdateDestroyAPIView, LC_ContactoVisitaRetrieveUpdateDestroyAPIView, COL_DRRRetrieveUpdateDestroyAPIView, LC_DerechoRetrieveUpdateDestroyAPIView

urlpatterns = [
    
    path('predio_copropiedad/',cr_predio_copropiedadListCreateAPIView.as_view(), name='Prediocopropiedad_list_create'),
    path('DatosPHCondominio/',CR_DatosPHCondominioListCreateAPIView.as_view(), name='DatosPHCondominio_list_create'),
    path('DatosAdicionalesLevantamientoCatastral/',LC_DatosAdicionalesLevantamientoCatastralListCreateAPIView.as_view(), name='DatosAdicionalesLevantamientoCatastral_list_create'),
    path('ContactoVisita/',LC_ContactoVisitaListCreateAPIView.as_view(), name='ContactoVisita_list_create'),
    path('DRR/',COL_DRRListCreateAPIView.as_view(), name='DRR_list_create'),
    path('Derecho/',LC_DerechoListCreateAPIView.as_view(), name='Derecho_list_create'),
    path('predio_copropiedad/<int:pk>/',cr_predio_copropiedadRetrieveUpdateDestroyAPIView.as_view(), name='predio_copropiedad_retrieve_update_delete'),
    path('DatosPHCondominio/<int:pk>/', CR_DatosPHCondominioRetrieveUpdateDestroyAPIView.as_view(), name='DatosPHCondominio_retrieve_update_delete'),
    path('DatosAdicionalesLevantamientoCatastral/<int:pk>/', LC_DatosAdicionalesLevantamientoCatastralRetrieveUpdateDestroyAPIView.as_view(), name='DatosAdicionalesLevantamientoCatastral_retrieve_update_delete'),
    path('ContactoVisita/<int:pk>/', LC_ContactoVisitaRetrieveUpdateDestroyAPIView.as_view(), name='ContactoVisita_retrieve_update_delete'),
    path('DRR/<int:pk>/', COL_DRRRetrieveUpdateDestroyAPIView.as_view(), name='DRR_retrieve_update_delete'),
    path('Derecho/<int:pk>/', LC_DerechoRetrieveUpdateDestroyAPIView.as_view(), name='Derecho_retrieve_update_delete'),
 
]