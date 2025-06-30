from django.urls import path
from apps.soporte_documental.api.views import COL_FuenteListApiView, COL_FuenteAdministrativaListApiView, LC_FuenteAdministrativaListApiView, COL_FuenteEspacialListApiView, CR_FuenteEspacialListApiView
from apps.soporte_documental.api.views import COL_FuenteCreateAPIView, COL_FuenteAdministrativaCreateAPIView, LC_FuenteAdministrativaCreateAPIView, COL_FuenteEspacialCreateAPIView, CR_FuenteEspacialCreateAPIView
from apps.soporte_documental.api.views import COL_FuenteRetrieveAPIView, COL_FuenteAdministrativaRetrieveAPIView, LC_FuenteAdministrativaRetrieveAPIView, COL_FuenteEspacialRetrieveAPIView, CR_FuenteEspacialRetrieveAPIView
from apps.soporte_documental.api.views import COL_FuenteDestroyAPIView, COL_FuenteAdministrativaDestroyAPIView, LC_FuenteAdministrativaDestroyAPIView, COL_FuenteEspacialDestroyAPIView, CR_FuenteEspacialDestroyAPIView
from apps.soporte_documental.api.views import COL_FuenteUpdateAPIView, COL_FuenteAdministrativaUpdateAPIView, LC_FuenteAdministrativaUpdateAPIView, COL_FuenteEspacialUpdateAPIView, CR_FuenteEspacialUpdateAPIView

urlpatterns = [
    path('COLFuente/list/', COL_FuenteListApiView.as_view(), name='Fuente_list'),
    path('COLFuenteAdministrativa/list/', COL_FuenteAdministrativaListApiView.as_view(), name='FuenteAdministrativaCOL_list'),
    path('LCFuenteAdministrativa/list/', LC_FuenteAdministrativaListApiView.as_view(), name='FuenteAdministrativaLC_list'),
    path('COLFuenteEspacial/list/', COL_FuenteEspacialListApiView.as_view(), name='FuenteEspacialCOL_list'),
    path('CRFuenteEspacial/list/', CR_FuenteEspacialListApiView.as_view(), name='FuenteEspacialCR_list'),

    path('COLFuente/create/', COL_FuenteCreateAPIView.as_view(), name='Fuente_create'),
    path('COLFuenteAdministrativa/create/', COL_FuenteAdministrativaCreateAPIView.as_view(), name='FuenteAdministrativaCOL_create'),
    path('LCFuenteAdministrativa/create/', LC_FuenteAdministrativaCreateAPIView.as_view(), name='FuenteAdministrativaLC_create'),
    path('COLFuenteEspacial/create/', COL_FuenteEspacialCreateAPIView.as_view(), name='FuenteEspacialCOL_create'),
    path('CRFuenteEspacial/create/', CR_FuenteEspacialCreateAPIView.as_view(), name='FuenteEspacialCR_create'),

    path('COLFuente/retrieve/<int:pk>/', COL_FuenteRetrieveAPIView.as_view(), name='Fuente_retrieve'),
    path('COLFuenteAdministrativa/retrieve/<int:pk>/', COL_FuenteAdministrativaRetrieveAPIView.as_view(), name='FuenteAdministrativaCOL_retrieve'),
    path('LCFuenteAdministrativa/retrieve/<int:pk>/', LC_FuenteAdministrativaRetrieveAPIView.as_view(), name='FuenteAdministrativaLC_retrieve'),
    path('COLFuenteEspacial/retrieve/<int:pk>/', COL_FuenteEspacialRetrieveAPIView.as_view(), name='FuenteEspacialCOL_retrieve'),
    path('CRFuenteEspacial/retrieve/<int:pk>/', CR_FuenteEspacialRetrieveAPIView.as_view(), name='FuenteEspacialCR_retrieve'),

    path('COLFuente/destroy/<int:pk>/', COL_FuenteDestroyAPIView.as_view(), name='Fuente_destroy'),
    path('COLFuenteAdministrativa/destroy/<int:pk>/', COL_FuenteAdministrativaDestroyAPIView.as_view(), name='FuenteAdministrativaCOL_destroy'),
    path('LCFuenteAdministrativa/destroy/<int:pk>/', LC_FuenteAdministrativaDestroyAPIView.as_view(), name='FuenteAdministrtaivaLC_destroy'),
    path('COLFuenteEspacial/destroy/<int:pk>/', COL_FuenteEspacialDestroyAPIView.as_view(), name='FuenteEspacialCOL_destroy'),
    path('CRFuenteEspacial/destroy/<int:pk>/', CR_FuenteEspacialDestroyAPIView.as_view(), name='FuenteEspacialCR_destroy'),

    path('COLFuente/update/<int:pk>/', COL_FuenteUpdateAPIView.as_view(), name='Fuente_update'),
    path('COLFuenteAdministrativa/update/<int:pk>/', COL_FuenteAdministrativaUpdateAPIView.as_view(), name='FuenteAdministrativaCOL_update'),
    path('LCFuenteAdmnistrativa/update/<int:pk>/', LC_FuenteAdministrativaUpdateAPIView.as_view(), name='FuenteAdministrativaLC_update'),
    path('COLFuenteEspacial/update/<int:pk>/', COL_FuenteEspacialUpdateAPIView.as_view(), name='FuenteEspacialCOL_update'),
    path('CRFuenteEspacial/update/<int:pk>/', CR_FuenteEspacialUpdateAPIView.as_view(), name='FuenteEspacialCR_update'),

]