from django.urls import path
from apps.paquete_interesados.api.views import COL_InteresadoListApiView, CR_InteresadoListApiVIew, COL_AgrupacionInteresadosLisApiView, col_miembrosListAPIView, CR_AgrupacionInteresadosListAPIView, LC_InteresadoContactoListAPIView
from apps.paquete_interesados.api.views import COL_InteresadoCreateAPIVIew, CR_InteresadoCreateAPIView, COL_AgrupacionInteresadosCreateAPIView, col_miembrosCreateAPIView, CR_AgrupacionInteresadosCreateAPIView, LC_InteresadoContactoCreateAPIView
from apps.paquete_interesados.api.views import COL_InteresadoRetrieveAPIView, CR_InteresadoRetrieveAPIView, COL_AgrupacionInteresadosRetrieveAPIView, col_miembrosRetrieveAPIView, CR_AgrupacionInteresadosRetrieveAPIView, LC_InteresadoContactoRetrieveAPIView
from apps.paquete_interesados.api.views import COL_InteresadoDestroyAPIVIew, CR_InteresadoDestroyAPIView, COL_AgrupacionInteresadosDestroyAPIView, col_miembrosDestroyAPIView, CR_AgrupacionInteresadosDestroyAPIView, LC_InteresadoContactoDestroy
from apps.paquete_interesados.api.views import COL_InteresadoUpdateAPIView, CR_InteresadoUpdateAPIView, COL_AgrupacionInteresadosUpdateAPIView, col_miembrosUpdateAPIView, CR_AgrupacionInteresadosUpdateAPIView, LC_InteresadoContactoUpdateAPIView

urlpatterns = [
    path('COLInteresado/list/', COL_InteresadoListApiView.as_view(), name='InteresadoCOL_list'),
    path('CRInteresado/list/', CR_InteresadoListApiVIew.as_view(), name='InteresadoCR_list'),
    path('COLAgrupacionInteresados/list/', COL_AgrupacionInteresadosLisApiView.as_view(), name='AgrupacionInteresadosCOL_list'),
    path('Miembros/list/', col_miembrosListAPIView.as_view(), name='Miembros_list'),
    path('CRAgrupacionInteresados/list/', CR_AgrupacionInteresadosListAPIView.as_view(), name='AgrupacionInteresadosCR_list'),
    path('InteresadoContacto/list/', LC_InteresadoContactoListAPIView.as_view(), name='InteresadosContacto_list'),

    path('COLInteresado/create/', COL_InteresadoCreateAPIVIew.as_view(), name='InteresadoCOL_create'),
    path('CRInteresado/create/', CR_InteresadoCreateAPIView.as_view(), name='InteresadoCR_create'),
    path('COLAgrupacionInteresados/create/', COL_AgrupacionInteresadosCreateAPIView.as_view(), name='AgrupacionInteresadosCOL_create'),
    path('Miembros/create/', col_miembrosCreateAPIView.as_view(), name='Miembros_create'),
    path('CRAgrupacionInteresados/create/', CR_AgrupacionInteresadosCreateAPIView.as_view(), name='AgrupacionInteresadoCR_created'),
    path('InteresadoContacto/create/', LC_InteresadoContactoCreateAPIView.as_view(), name='InteresadoContacto_create'),

    path('COLInteresado/retrieve/<int:pk>/', COL_InteresadoRetrieveAPIView.as_view(), name='InteresadoCOL_retrieve'),
    path('CRInteresado/retrieve/<int:pk>/', CR_InteresadoRetrieveAPIView.as_view(), name='InteresadoCR_retrieve'),
    path('COLAgrupacionInteresados/retrieve/<int:pk>/', COL_AgrupacionInteresadosRetrieveAPIView.as_view(), name='AgrupacionInteresadosCOL_retrieve'),
    path('Miembros/retrieve/<int:pk>/', col_miembrosRetrieveAPIView.as_view(), name='Miembros_retrieve'),
    path('CRAgrupacionInteresados/retrieve/<int:pk>/', CR_AgrupacionInteresadosRetrieveAPIView.as_view(), name='AgrupacionInteresadosCR_retrieve'),
    path('InteresadoContacto/retrieve/<int:pk>/', LC_InteresadoContactoRetrieveAPIView.as_view(), name='InteresadosContacto_retrieve'),

    path('COLInteresado/destroy/<int:pk>/', COL_InteresadoDestroyAPIVIew.as_view(), name='InteresadoCOL_destroy'),
    path('CRInteresado/destroy/<int:pk>/', CR_InteresadoDestroyAPIView.as_view(), name='InteresadoCR_destroy'),
    path('COLAgrupacionInteresados/destroy/<int:pk>/', COL_AgrupacionInteresadosDestroyAPIView.as_view(), name='AgrupacionInteresadosCOL_destroy'),
    path('Miembros/destroy/<int:pk>/', col_miembrosDestroyAPIView.as_view(), name='Miembros_destroy'),
    path('CRAgrupacionInteresados/destroy/<int:pk>/', CR_AgrupacionInteresadosDestroyAPIView.as_view(), name='AgrupacionInteresadosCR_destroy'),
    path('InteresadoContacto/destroy/<int:pk>/', LC_InteresadoContactoDestroy.as_view(), name='InteresadoContacto_destroy'),

    path('COLInteresado/update/<int:pk>/', COL_InteresadoUpdateAPIView.as_view(), name='InteresadoCOL_update'),
    path('CRInteresado/update/<int:pk>/', CR_InteresadoUpdateAPIView.as_view(), name='InteresadoCR_update'),
    path('COLAgrupacionInteresados/update/<int:pk>/', COL_AgrupacionInteresadosUpdateAPIView.as_view(), name='AgrupacionInteresadosCR_update'),
    path('Miembros/update/<int:pk>/', col_miembrosUpdateAPIView.as_view(), name='Miembros_update'),
    path('CRAgrupacionInteresados/update/<int:pk>/', CR_AgrupacionInteresadosUpdateAPIView.as_view(), name='AgrupacionInteresadosCR_update'),
    path('InteresadoContacto/update/<int:pk>/', LC_InteresadoContactoUpdateAPIView.as_view(), name='InteresadoContacto_update'),
]