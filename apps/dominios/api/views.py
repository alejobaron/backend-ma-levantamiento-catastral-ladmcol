from rest_framework import viewsets
from rest_framework.response import Response
from apps.dominios.models import COL_UnidadAdministrativaBasicaTipo, LC_PredioTipo, LC_CondicionPredioTipo, LC_DestinacionEconomicaTipo, LC_ResultadoVisitaTipo, CR_DocumentoTipo, LC_DerechoTipo, CR_InteresadoTipo, CR_SexoTipo, CR_GrupoEtnicoTipo, COL_GrupoInteresadoTipo, COL_EstadoDisponibilidadTipo, CI_Forma_Presentacion_Codigo, COL_FuenteAdministrativaTipo, LC_FuenteAdministrativaTipo, COL_FuenteEspacialTipo, COL_DimensionTipo, COL_RelacionSuperficieTipo, CR_UnidadConstruccionTipo, CR_UsoUConsTipo, CR_ConstruccionPlantaTipo
from apps.dominios.api.serializer import COL_UnidadAdministrativaBasicaTipoSerializer, LC_PredioTipoSerializer, LC_CondicionPredioTipoSerializer, LC_DestinacionEconomicaTipoSerializer, LC_ResultadoVisitaTipoSerializer, CR_DocumentoTipoSerializer, LC_DerechoTipoSerializer, CR_InteresadoTipoSerializer, CR_SexoTipoSerializer, CR_GrupoEtnicoTipoSerializer, COL_GrupoInteresadoTipoSerializer, COL_EstadoDisponibilidadTipoSerializer, CI_Forma_Presentacion_CodigoSerializer, COL_FuenteAdministrativaTipoSerializer, LC_FuenteAdministrativaTipoSerializer, COL_FuenteEspacialTipoSerializer, COL_DimensionTipoSerializer, COL_RelacionSuperficieTipoSerializer, CR_UnidadConstruccionTipoSerializer, CR_UsoUConsTipoSerializer, CR_ConstruccionPlantaTipoSerializer
""" class TipoUABChoicesAPIView(APIView):
    def get(self, request):
        choices = COL_UnidadAdministrativaBasicaTipo.Tipo.choices
        return Response([{"valor": valor, "etiqueta": etiqueta} for valor, etiqueta in choices]) """


class COL_UnidadAdministrativaBasicaTipoViewSet(viewsets.ModelViewSet):
    queryset = COL_UnidadAdministrativaBasicaTipo.objects.filter(state=True)
    serializer_class = COL_UnidadAdministrativaBasicaTipoSerializer
    """ permission_classes = [IsAuthenticated] """
    
class LC_PredioTipoViewSet(viewsets.ModelViewSet):
    queryset = LC_PredioTipo.objects.filter(state=True)
    serializer_class = LC_PredioTipoSerializer
    
class LC_CondicionPredioTipoViewSet(viewsets.ModelViewSet):
    queryset = LC_CondicionPredioTipo.objects.filter(state=True)
    serializer_class = LC_CondicionPredioTipoSerializer
    
class LC_DestinacionEconomicaViewSet(viewsets.ModelViewSet):
    queryset = LC_DestinacionEconomicaTipo.objects.filter(state=True)
    serializer_class = LC_DestinacionEconomicaTipoSerializer
    
class LC_ResultadoVisitaViewSet(viewsets.ModelViewSet):
    queryset = LC_ResultadoVisitaTipo.objects.filter(state=True)
    serializer_class = LC_ResultadoVisitaTipoSerializer
    
class CR_DocumentoTipoViewSet(viewsets.ModelViewSet):
    queryset = CR_DocumentoTipo.objects.filter(state=True)
    serializer_class = CR_DocumentoTipoSerializer

class LC_DerechoTipoViewSet(viewsets.ModelViewSet):
    queryset = LC_DerechoTipo.objects.filter(state=True)
    serializer_class = LC_DerechoTipoSerializer
    
class CR_InteresadoTipoViewSet(viewsets.ModelViewSet):
    queryset = CR_InteresadoTipo.objects.filter(state=True)
    serializer_class = CR_InteresadoTipoSerializer
    
class CR_SexoTipoViewSet(viewsets.ModelViewSet):
    queryset = CR_SexoTipo.objects.filter(state=True)
    serializer_class = CR_SexoTipoSerializer
    
class CR_GrupoEtnicoTipoViewSet(viewsets.ModelViewSet):
    queryset = CR_GrupoEtnicoTipo.objects.filter(state=True)
    serializer_class = CR_GrupoEtnicoTipoSerializer
    
class COL_GrupoInteresadoTipoViewSet(viewsets.ModelViewSet):
    queryset = COL_GrupoInteresadoTipo.objects.filter(state=True)
    serializer_class = COL_GrupoInteresadoTipoSerializer
    
class COL_EstadoDisponibilidadTipoViewSet(viewsets.ModelViewSet):
    queryset = COL_EstadoDisponibilidadTipo.objects.filter(state=True)
    serializer_class = COL_EstadoDisponibilidadTipoSerializer
    
class CI_Forma_Presentacion_CodigoViewSet(viewsets.ModelViewSet):
    queryset = CI_Forma_Presentacion_Codigo.objects.filter(state=True)
    serializer_class = CI_Forma_Presentacion_CodigoSerializer
    
class COL_FuenteAdministrativaTipoViewSet(viewsets.ModelViewSet):
    queryset = COL_FuenteAdministrativaTipo.objects.filter(state=True)
    serializer_class = COL_FuenteAdministrativaTipoSerializer
    
class LC_FuenteAdministrativaTipoViewSet(viewsets.ModelViewSet):
    queryset = LC_FuenteAdministrativaTipo.objects.filter(state=True)
    serializer_class = LC_FuenteAdministrativaTipoSerializer
    
class COL_FuenteEspacialTipoViewSet(viewsets.ModelViewSet):
    queryset = COL_FuenteEspacialTipo.objects.filter(state=True)
    serializer_class = COL_FuenteEspacialTipoSerializer
    
class COL_DimensionTipoViewSet(viewsets.ModelViewSet):
    queryset = COL_DimensionTipo.objects.filter(state=True)
    serializer_class = COL_DimensionTipoSerializer
    
class COL_RelacionSuperficieTipoViewSet(viewsets.ModelViewSet):
    queryset = COL_RelacionSuperficieTipo.objects.filter(state=True)
    serializer_class = COL_RelacionSuperficieTipoSerializer
    
class CR_UnidadConstruccionTipoViewSet(viewsets.ModelViewSet):
    queryset = CR_UnidadConstruccionTipo.objects.filter(state=True)
    serializer_class = CR_UnidadConstruccionTipoSerializer   
    
class CR_UsoUConsTipoViewSet(viewsets.ModelViewSet):
    queryset = CR_UsoUConsTipo.objects.filter(state=True)
    serializer_class = CR_UsoUConsTipoSerializer   

class CR_ConstruccionPlantaTipoViewSet(viewsets.ModelViewSet):
    queryset = CR_ConstruccionPlantaTipo.objects.filter(state=True)
    serializer_class = CR_ConstruccionPlantaTipoSerializer   




    

 

    
    
    
    
    
    




