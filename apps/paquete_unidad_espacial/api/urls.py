from django.urls import path
from apps.paquete_unidad_espacial.api.views import COL_UnidadEspacialListApiView, CR_ConstruccionListApiView, CR_CaracteristicasUnidadConstruccionListApiView, CR_UnidadConstruccionListApiView, CR_TerrenoListApiView
from apps.paquete_unidad_espacial.api.views import COL_UnidadEspacialCreateAPIView, CR_ConstruccionCreateAPIView, CR_CaracteristicasUnidadConstruccionCreateAPIView, CR_UnidadConstruccionCreateAPIView, CR_TerrenoCreateAPIView
from apps.paquete_unidad_espacial.api.views import COL_UnidadEspacialRetrieveAPIView, CR_ConstruccionRetrieveAPIiew, CR_CaracteristicasUnidadConstruccionRetrieveAPIView, CR_UnidadConstruccionRetrieveAPIView, CR_TerrenoRetrieveAPIView
from apps.paquete_unidad_espacial.api.views import COL_UnidadEspacialDestroyAPIView, CR_ConstruccionDestroyAPIView, CR_CaracteristicasUnidadConstruccionDestroyApPIView, CR_UnidadConstruccionDestroyAPIView, CR_TerrenoDestroyAPIView

urlpatterns = [
    path('UnidadEspacial/list/', COL_UnidadEspacialListApiView.as_view(), name='UnidadEspacial_list'),
    path('Construccion/list/', CR_ConstruccionListApiView.as_view(), name='Construccion_list'),
    path('CaracteristicasUnidadConstruccion', CR_CaracteristicasUnidadConstruccionListApiView.as_view(), name='CaracteristicasUnidadConstruccion_list'),
    path('UnidadConstruccion/list/', CR_UnidadConstruccionListApiView.as_view(), name='UnidadConstruccion_list'),
    path('Terreno/list/', CR_TerrenoListApiView.as_view(), name='Terreno_list'),

    path('UnidadEspacial/create/', COL_UnidadEspacialCreateAPIView.as_view(), name='UnidadEspacial_create'),
    path('Construccion/create/', CR_ConstruccionCreateAPIView.as_view(), name='Construccion_create'),
    path('CaracteristicasUnidadConstruccion/create/', CR_CaracteristicasUnidadConstruccionCreateAPIView.as_view(), name='CaracteristicasUnidadConstruccion_create'),
    path('UnidadConstruccion/create/', CR_UnidadConstruccionCreateAPIView.as_view(), name='UnidadConstruccion_create'),
    path('Terreno/create/',CR_TerrenoCreateAPIView.as_view(), name='Terreno_create'),

    path('UnidadEspacila/retrieve/<int:pk>/', COL_UnidadEspacialRetrieveAPIView.as_view(), name='UnidadEspacial_retrieve'),
    path('Construccion/retrieve/<int:pk>/', CR_ConstruccionRetrieveAPIiew.as_view(), name='Construccion_retrieve'),
    path('CaracteristicasUnidadConstruccion/retrieve/<int_pk>/', CR_CaracteristicasUnidadConstruccionRetrieveAPIView.as_view(), name='CaracteristicasUnidadConstruccion_retrieve'),
    path('UnidadCOnstruccion/retrieve/<int:pk>/', CR_UnidadConstruccionRetrieveAPIView.as_view(), name = 'Unidad_Construccion_retrieve'),
    path('Terreno/retrive/<int:pk>/', CR_TerrenoRetrieveAPIView.as_view(), name='Terreno_retrieve'),

    path('UnidadEspacial/destroy/<int:pk>/', COL_UnidadEspacialDestroyAPIView.as_view(), name='UnidadEspacial_destroy'),
    path('Construccion/destroy/<int:pk>/', CR_ConstruccionDestroyAPIView.as_view(), name='Construccion_destroy'),
    path('CaracteristicasUnidadConstruccion/destroy/<int:pk>/', CR_CaracteristicasUnidadConstruccionDestroyApPIView.as_view(), name='CaracteristicasUidadConstruccion_destroy'),
    path('UnidadConstruccion/destroy/<int:pk>/', CR_UnidadConstruccionDestroyAPIView.as_view(), name='UnidadConstruccion_destroy'),
    path('Terreno/destroy/<int:pk>/', CR_TerrenoDestroyAPIView.as_view(), name='Terreno_destroy')    
]