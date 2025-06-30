"""
URL configuration for MA_LEVANTAMIENTO_CATASTRAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.views import Login, Logout

schema_view = get_schema_view(
   openapi.Info(
      title="Documentación de API",
      default_version='v0.1',
      description="Documentación pública de Modelo de Aplicación Levantamiento Catastral",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="alejobaron.geomatica@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('logout/', Logout.as_view(), name='logout'),
    path('login/', Login.as_view(), name='Login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('usuario/', include('apps.users.api.routers')),
    path('paquete_administrativo/',include('apps.paquete_administrativo.api.routers')),
    path('paquete_interesados/', include('apps.paquete_interesados.api.routers')),
    path('paquete_unidad_espacial/', include('apps.paquete_unidad_espacial.api.routers')),
    path('soporte_documental/', include('apps.soporte_documental.api.routers')),
    path("estructura/",include('apps.estructuras.api.routers')),
    path("dominios/",include('apps.dominios.api.routers')),
]

