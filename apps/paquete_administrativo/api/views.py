from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.paquete_administrativo.api.serializer import COL_UnidadAdministrativaBasicaSerializer, LC_PredioSerializer, cr_predio_copropiedadSerializer, CR_DatosPHCondominioSerializer, LC_DatosAdicionalesLevantamientoCatastralSerializer, LC_ContactoVisitaSerializer, COL_DRRSerializer, LC_DerechoSerializer
from apps.paquete_administrativo.api.access_policy import GeneralAccessPolicy

class COL_UnidadAdministrativaBasicaViewSet(viewsets.ModelViewSet):
    serializer_class = COL_UnidadAdministrativaBasicaSerializer
    permission_classes = (IsAuthenticated,)
    access_policy = GeneralAccessPolicy()

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
        
    def list(self,request):
        COL_UnidadAdministativaBasica_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(COL_UnidadAdministativaBasica_serializer.data, status = status.HTTP_200_OK)
        
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Unidad Administrativa Basica creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            COL_UnidadAdministativaBasica_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if COL_UnidadAdministativaBasica_serializer.is_valid():
                COL_UnidadAdministativaBasica_serializer.save()
                return Response(COL_UnidadAdministativaBasica_serializer.data, status = status.HTTP_200_OK)
            return Response(COL_UnidadAdministativaBasica_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        COL_UnidadAdministrativaBasica = self.get_queryset().filter(id=pk).first()
        if COL_UnidadAdministrativaBasica:
            COL_UnidadAdministrativaBasica.state = False
            COL_UnidadAdministrativaBasica.save()
            return Response({'message':'Unidad Administrativa Basica eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Unidad Administraitva Basica con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class LC_PredioViewSet(viewsets.ModelViewSet):
    serializer_class = LC_PredioSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        LC_Predio_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(LC_Predio_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Predio creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            LC_Predio_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if LC_Predio_serializer.is_valid():
                LC_Predio_serializer.save()
                return Response(LC_Predio_serializer.data, status = status.HTTP_200_OK)
        return Response(LC_Predio_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        LC_Predio = self.get_queryset().filter(id=pk).first()
        if LC_Predio:
            LC_Predio.state = False
            LC_Predio.save()
            return Response({'message':'Predio eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Predio con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class cr_predio_copropiedadViewSet(viewsets.ModelViewSet):
    serializer_class = cr_predio_copropiedadSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
        
    def list(self,request):
        cr_predio_copropiedad_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(cr_predio_copropiedad_serializer.data, status = status.HTTP_200_OK)
        
    def creeate(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Predio en copropiedad creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            cr_predio_copropiedad_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if cr_predio_copropiedad_serializer.is_valid():
                cr_predio_copropiedad_serializer.save()
                return Response(cr_predio_copropiedad_serializer.data, status = status.HTTP_200_OK)
            return Response(cr_predio_copropiedad_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        cr_predio_copropiedad = self.get_queryset().filter(id=pk).first()
        if cr_predio_copropiedad:
            cr_predio_copropiedad.state = False
            cr_predio_copropiedad.save()
            return Response({'message':'Predio en copropiedad eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No esxiste predio en copropiedad con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class CR_DatosPHCondominioViewSet(viewsets.ModelViewSet):
    serializer_class = CR_DatosPHCondominioSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
        
    def list(self,request):
        CR_DatosPHCondominio_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(CR_DatosPHCondominio_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos de PH/Condominio creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            CR_DatosPHCondominio_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if CR_DatosPHCondominio_serializer.is_valid():
                CR_DatosPHCondominio_serializer.save()
                return Response(CR_DatosPHCondominio_serializer.data, status = status.HTTP_200_OK)
            return Response(CR_DatosPHCondominio_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        CR_DatosPHCondominio = self.get_queryset().filter(id=pk).first()
        if CR_DatosPHCondominio:
            CR_DatosPHCondominio.state = False
            CR_DatosPHCondominio.save()
            return Response({'message':'Datos de PH/Condominio eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'message': 'No existe datos de PH/Condominio con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class LC_DatosAdicionalesLevantamientoCatastralViewSet(viewsets.ModelViewSet):
    serializer_class = LC_DatosAdicionalesLevantamientoCatastralSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
        
    def list(self,request):
        LC_DatosAdicionalesLevantamientoCatastral_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(LC_DatosAdicionalesLevantamientoCatastral_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos adicionales de levanatamiento catastral creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            LC_DatosAdicionalesLevantamientoCatastral_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if LC_DatosAdicionalesLevantamientoCatastral_serializer.is_valid():
                LC_DatosAdicionalesLevantamientoCatastral_serializer.save()
                return Response(LC_DatosAdicionalesLevantamientoCatastral_serializer.data, status = status.HTTP_200_OK)
            return Response(LC_DatosAdicionalesLevantamientoCatastral_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request, pk=None):
        LC_DatosAdicionalesLevantamientoCatastral = self.get_queryset().filter(id=pk).first()
        if LC_DatosAdicionalesLevantamientoCatastral:
            LC_DatosAdicionalesLevantamientoCatastral.state = False
            LC_DatosAdicionalesLevantamientoCatastral.save()
            return Response({'message':'Datos adicionales de levantamiento catastral eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe datos adicionales de levantamiento catastral con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class LC_ContactoVisitaViewSet(viewsets.ModelViewSet):
    serializer_class = LC_ContactoVisitaSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
        
    def list(self,request):
        LC_ContactoVisita_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(LC_ContactoVisita_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Contacto de visita creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            LC_ContactoVisita_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if LC_ContactoVisita_serializer.is_valid():
                LC_ContactoVisita_serializer.save()
                return Response(LC_ContactoVisita_serializer.data, status = status.HTTP_200_OK)
            return Response(LC_ContactoVisita_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        LC_ContactoVisita = self.get_queryset().filter(id=pk).first()
        if LC_ContactoVisita:
            LC_ContactoVisita.state = False
            LC_ContactoVisita.save()
            return Response({'message':'Contacto de Visita eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe contacto de visita con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class COL_DRRViewSet(viewsets.ModelViewSet):
    serializer_class = COL_DRRSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
        
    def list(self,request):
        COL_DRR_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(COL_DRR_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Derechos, Responsabilidades y Restricciones creados correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            COL_DRR_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if COL_DRR_serializer.is_valid():
                COL_DRR_serializer.save()
                return Response(COL_DRR_serializer.data, status = status.HTTP_200_OK)
            return Response(COL_DRR_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        COL_DRR =self.get_queryset().filter(id=pk).first()
        if COL_DRR:
            COL_DRR.state = False
            COL_DRR.save()
            return Response({'message':'Derechos, Responsabilidades y Restriccones eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Derechos, Responsabilidades y Restricciones con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class LC_DerechoViewSet(viewsets.ModelViewSet):
    serializer_class = LC_DerechoSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
        
    def list(self,request):
        LC_Derecho_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(LC_Derecho_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Derecho creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            LC_Derecho_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if LC_Derecho_serializer.is_valid():
                LC_Derecho_serializer.save()
                return Response(LC_Derecho_serializer.data, status = status.HTTP_200_OK)
            return Response(LC_Derecho_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        LC_Derecho = self.get_queryset().filter(id=pk).first()
        if LC_Derecho:
            LC_Derecho.status = False
            LC_Derecho.save()
            return Response({'message':'Derecho eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Derecho con estos datos'}, status = status.HTTP_400_BAD_REQUEST) 
