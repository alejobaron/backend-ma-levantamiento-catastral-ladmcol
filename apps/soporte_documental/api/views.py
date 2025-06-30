from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response 

from apps.base.api import GeneralListApiView
from apps.soporte_documental.api.serializer import COL_FuenteSerializer, COL_FuenteAdministrativaSerializer, LC_FuenteAdministrativaSerializer, COL_FuenteEspacialSerializer, CR_FuenteEspacialSerializer

class COL_FuenteViewSet(viewsets.ModelViewSet):
    serializer_class = COL_FuenteSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        COL_Fuente_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(COL_Fuente_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Fuente creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            COL_Fuente_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if COL_Fuente_serializer.is_valid():
                COL_Fuente_serializer.save()
                return Response(COL_Fuente_serializer.data, status = status.HTTP_200_OK)
            return Response(COL_Fuente_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        COL_Fuente = self.get_queryset().filter(id=pk).first()
        if COL_Fuente:
            COL_Fuente.state = False
            COL_Fuente.save()
            return Response({'message':'Fuente eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Fuente con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class COL_FuenteAdministrativaViewSet(viewsets.ModelViewSet):
    serializer_class = COL_FuenteAdministrativaSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        COL_FuenteAdministrativa_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(COL_FuenteAdministrativa_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Fuente Administrativa (COL) creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            COL_FuenteAdministrativa_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if COL_FuenteAdministrativa_serializer.is_valid():
                COL_FuenteAdministrativa_serializer.save()
                return Response(COL_FuenteAdministrativa_serializer.data, status = status.HTTP_200_OK)
            return Response(COL_FuenteAdministrativa_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
  
    
    def destroy(self, request, pk=None):
        COL_FuenteAdministrativa = self.get_queryset().filter(id=pk).first()
        if COL_FuenteAdministrativa:
            COL_FuenteAdministrativa.state = False
            COL_FuenteAdministrativa.save()
            return Response({'message':'Fuente Administrativa (COL) eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Fuente Administrativa (COL) con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class LC_FuenteAdministrativaViewSet(viewsets.ModelViewSet):
    serializer_class = LC_FuenteAdministrativaSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        LC_FuenteAdministrativa_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(LC_FuenteAdministrativa_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Fuente Administrativa (LC) creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            LC_FuenteAdministrativa_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if LC_FuenteAdministrativa_serializer.is_valid():
                LC_FuenteAdministrativa_serializer.save()
                return Response(LC_FuenteAdministrativa_serializer.data, status = status.HTTP_200_OK)
            return Response(LC_FuenteAdministrativa_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        LC_FuenteAdministrativa = self.get_queryset().filter(id=pk).first()
        if LC_FuenteAdministrativa:
            LC_FuenteAdministrativa.state = False
            LC_FuenteAdministrativa.save()
            return Response({'message':'Fuente Administrativa (LC) eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Fuente Administrativa (LC) con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class COL_FuenteEspacialViewSet(viewsets.ModelViewSet):
    serializer_class = COL_FuenteEspacialSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        COL_FuenteEspacial_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(COL_FuenteEspacial_serializer.data, status = status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Fuente Espacial (COL) creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            COL_FuenteEspacial_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if COL_FuenteEspacial_serializer.is_valid():
                COL_FuenteEspacial_serializer.save()
                return Response(COL_FuenteEspacial_serializer.data, status = status.HTTP_200_OK)
            return Response(COL_FuenteEspacial_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        COL_FuenteEspacial = self.get_queryset().filter(id=pk).first()
        if COL_FuenteEspacial:
            COL_FuenteEspacial.state = False
            COL_FuenteEspacial.save()
            return Response({'message':'Fuente Espacial (COL) eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Fuente Espacial (COL) con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

class CR_FuenteEspacialViewSet(viewsets.ModelViewSet):
    serializer_class = CR_FuenteEspacialSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        CR_FuenteEspacial_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(CR_FuenteEspacial_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Fuente ESpacial (CR) creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            CR_FuenteEspacial_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if CR_FuenteEspacial_serializer.is_valid():
                CR_FuenteEspacial_serializer.save()
                return Response(CR_FuenteEspacial_serializer.data, status = status.HTTP_200_OK)
            return Response(CR_FuenteEspacial_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        CR_FuenteEspacial = self.get_queryset().filter(id=pk).first()
        if CR_FuenteEspacial:
            CR_FuenteEspacial.state = False
            CR_FuenteEspacial.save()
            return Response({'message':'Fuente Espacial (CR) eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Fuente Espacial (CR) con estos datos'}, status = status.HTTP_400_BAD_REQUEST)