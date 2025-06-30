from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.estructuras.api.serializer import ExtDireccionSerializer, ExtinteresadoSerializer, EstructuraNovedadNumeroPredialSerializer, NovedadFMISerializer, ExtArchivoSerializer, AreaValorSerializer, VolumenValorSerializer

class ExtInteresadoViewSet(viewsets.ModelViewSet):
    serializer_class = ExtinteresadoSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
        
    def list(self,request):
        ExtInteresado_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(ExtInteresado_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Interesado creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            ExtInteresado_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if ExtInteresado_serializer.is_valid():
                ExtInteresado_serializer.save()
                return Response(ExtInteresado_serializer.data, status = status.HTTP_200_OK)
            return Response(ExtInteresado_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe Interesado con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        ExtInteresado = self.get_queryset().filter(id=pk).first()
        if ExtInteresado:
            ExtInteresado.state = False
            ExtInteresado.save()
            return Response({'message':'Interesado eliminado correctamente'}, status= status.HTTP_200_OK)
        return Response({'error':'No existe interesado con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
    
class ExtDireccionViewSet(viewsets.ModelViewSet):
    serializer_class = ExtDireccionSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
        
    def list(self,request):
        ExtDireccion_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(ExtDireccion_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Dirección creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            ExtDireccion_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if ExtDireccion_serializer.is_valid():
                ExtDireccion_serializer.save()
                return Response(ExtDireccion_serializer.data, status = status.HTTP_200_OK)
            return Response(ExtDireccion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe Dirección con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        ExtDireccion = self.get_queryset().filter(id=pk).first()
        if ExtDireccion:
            ExtDireccion.state = False
            ExtDireccion.save()
            return Response({'message':'Dirección eliminada correctamente'}, status= status.HTTP_200_OK)
        return Response({'error':'No existe dirección con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
    
class EstructuraNovedadNumeroPredialViewSet(viewsets.ModelViewSet):
    serializer_class = EstructuraNovedadNumeroPredialSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
        
    def list(self,request):
        EstructuraNovedadNumeroPredial_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(EstructuraNovedadNumeroPredial_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Novedad número predial creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            EstructuraNovedadNumeroPredial_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if EstructuraNovedadNumeroPredial_serializer.is_valid():
                EstructuraNovedadNumeroPredial_serializer.save()
                return Response(EstructuraNovedadNumeroPredial_serializer.data, status = status.HTTP_200_OK)
            return Response(EstructuraNovedadNumeroPredial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe Novedad de número predial con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        EstructuraNovedadNumeroPredial = self.get_queryset().filter(id=pk).first()
        if EstructuraNovedadNumeroPredial:
            EstructuraNovedadNumeroPredial.state = False
            EstructuraNovedadNumeroPredial.save()
            return Response({'message':'Novedad número predial eliminada correctamente'}, status= status.HTTP_200_OK)
        return Response({'error':'No existe novedad número predial con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
    
class NovedadFMIViewSet(viewsets.ModelViewSet):
    serializer_class = NovedadFMISerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
        
    def list(self,request):
        NovedadFMI_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(NovedadFMI_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Novedad de FMI creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            NovedadFMI_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if NovedadFMI_serializer.is_valid():
                NovedadFMI_serializer.save()
                return Response(NovedadFMI_serializer.data, status = status.HTTP_200_OK)
            return Response(NovedadFMI_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe Novedad de FMI con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        NovedadFMI = self.get_queryset().filter(id=pk).first()
        if NovedadFMI:
            NovedadFMI.state = False
            NovedadFMI.save()
            return Response({'message':'Novedad de FMI eliminada correctamente'}, status= status.HTTP_200_OK)
        return Response({'error':'No existe novedad de FMI con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
    
class ExtArchivoSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = ExtArchivoSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
        
    def list(self,request):
        ExtArchivo_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(ExtArchivo_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Repositorio de archivo creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            ExtArchivo_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if ExtArchivo_serializer.is_valid():
                ExtArchivo_serializer.save()
                return Response(ExtArchivo_serializer.data, status = status.HTTP_200_OK)
            return Response(ExtArchivo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe Repositorio de archivo con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        ExtArchivo = self.get_queryset().filter(id=pk).first()
        if ExtArchivo:
            ExtArchivo.state = False
            ExtArchivo.save()
            return Response({'message':'Repositorio de archivo eliminado correctamente'}, status= status.HTTP_200_OK)
        return Response({'error':'No existe Repositorio de archivo con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
    
class AreaValorSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = AreaValorSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
        
    def list(self,request):
        AreaValor_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(AreaValor_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Valor de área creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            AreaValor_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if AreaValor_serializer.is_valid():
                AreaValor_serializer.save()
                return Response(AreaValor_serializer.data, status = status.HTTP_200_OK)
            return Response(AreaValor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe valor de área con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        AreaValor = self.get_queryset().filter(id=pk).first()
        if AreaValor:
            AreaValor.state = False
            AreaValor.save()
            return Response({'message':'Valor de área eliminado correctamente'}, status= status.HTTP_200_OK)
        return Response({'error':'No existe valor de área con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
    
class VolumenValorSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = VolumenValorSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
        
    def list(self,request):
        VolumenValor_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(VolumenValor_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Valor de volumen creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            VolumenValor_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if VolumenValor_serializer.is_valid():
                VolumenValor_serializer.save()
                return Response(VolumenValor_serializer.data, status = status.HTTP_200_OK)
            return Response(VolumenValor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe valor de volumen con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        VolumenValor = self.get_queryset().filter(id=pk).first()
        if VolumenValor:
            VolumenValor.state = False
            VolumenValor.save()
            return Response({'message':'Valor de volumen eliminado correctamente'}, status= status.HTTP_200_OK)
        return Response({'error':'No existe valor de volumen con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
