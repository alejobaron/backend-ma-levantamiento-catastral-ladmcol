from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.paquete_unidad_espacial.api.serializer import COL_UnidadEspacialSerializer, CR_ConstruccionSerializer, CR_CaracteristicasUnidadConstruccionSerializer, CR_UnidadConstruccionSerializer, CR_TerrenoSerializer


class COL_UnidadEspacialViewSet(viewsets.ModelViewSet):
    serializer_class = COL_UnidadEspacialSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        COL_UnidadEspacial_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(COL_UnidadEspacial_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Únidad Espacial creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            COL_UnidadEspacial_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if COL_UnidadEspacial_serializer.is_valid():
                COL_UnidadEspacial_serializer.save()
                return Response(COL_UnidadEspacial_serializer.data, status = status.HTTP_200_OK)
        return Response(COL_UnidadEspacial_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        COL_UnidadEspacial = self.get_queryset().filter(id=pk).first()
        if COL_UnidadEspacial:
            COL_UnidadEspacial.state = False
            COL_UnidadEspacial.save()
            return Response({'message':'Únidad espacial eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Únidad espacial con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

class CR_ConstruccionViewSet(viewsets.ModelViewSet):
    serializer_class = CR_ConstruccionSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        CR_Construccion_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(CR_Construccion_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Construcción creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            CR_Construccion_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if CR_Construccion_serializer.is_valid():
                CR_Construccion_serializer.save()
                return Response(CR_Construccion_serializer.data, status = status.HTTP_200_OK)
        return Response(CR_Construccion_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        CR_Construccion = self.get_queryset().filter(id=pk).first()
        if CR_Construccion:
            CR_Construccion.state = False
            CR_Construccion.save()
            return Response({'message':'Construcción eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Construcción con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

class CR_CaracteristicasUnidadConstruccionViewSet(viewsets.ModelViewSet):
    serializer_class = CR_CaracteristicasUnidadConstruccionSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        CR_CaracteristicasUnidadConstruccion_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(CR_CaracteristicasUnidadConstruccion_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Caracteristicas de la únidad de construcción creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            CR_CaracteristicasUnidadConstruccion_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if CR_CaracteristicasUnidadConstruccion_serializer.is_valid():
                CR_CaracteristicasUnidadConstruccion_serializer.save()
                return Response(CR_CaracteristicasUnidadConstruccion_serializer.data, status = status.HTTP_200_OK)
            return Response(CR_CaracteristicasUnidadConstruccion_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        CR_CaracteristicasUnidadConstruccion = self.get_queryset().filter(id=pk).first()
        if CR_CaracteristicasUnidadConstruccion:
            CR_CaracteristicasUnidadConstruccion.state = False
            CR_CaracteristicasUnidadConstruccion.save()
            return Response({'message':'Caracteristicas de la únidad de construcción eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe caracteristicas de la únidad de construccion con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
 
class CR_UnidadConstruccionViewSet(viewsets.ModelViewSet):
    serializer_class = CR_UnidadConstruccionSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        CR_UnidadConstruccion_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(CR_UnidadConstruccion_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Únidad de construcción creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            CR_UnidadConstruccion_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if CR_UnidadConstruccion_serializer.is_valid():
                CR_UnidadConstruccion_serializer.save()
                return Response(CR_UnidadConstruccion_serializer.data, status = status.HTTP_200_OK)
            return Response(CR_UnidadConstruccion_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy (self, request, pk=None):
        CR_UnidadCOnstruccion = self.get_queryset().filter(id=pk).first()
        if CR_UnidadCOnstruccion:
            CR_UnidadCOnstruccion.state = False
            CR_UnidadCOnstruccion.save()
            return Response({'message':'Únidad de construcción eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe únidad de construccion con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

class CR_TerrenoViewSet(viewsets.ModelViewSet):
    serializer_class = CR_TerrenoSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        CR_Terreno_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(CR_Terreno_serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Terreno creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            CR_Terreno_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if CR_Terreno_serializer.is_valid():
                CR_Terreno_serializer.save()
                return Response(CR_Terreno_serializer.data, status = status.HTTP_200_OK)
            return Response(CR_Terreno_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        CR_Terreno = self.get_queryset().filter(id=pk).first()
        if CR_Terreno:
            CR_Terreno.state = False
            CR_Terreno.save()
            return Response ({'message':'Terreno eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe terreno con estos datos'}, status = status.HTTP_400_BAD_REQUEST)