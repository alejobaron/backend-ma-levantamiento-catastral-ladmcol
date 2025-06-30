from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.users.authentication_mixins import Authentication 
from apps.paquete_interesados.api.serializer import COL_InteresadoSerializer, CR_InteresadoSerializer, COL_AgrupacionInteresadosSerializer, col_miembrosSerializer, CR_AgrupacionInteresadosSerializer, LC_InteresadoContactoSerializer

class COL_InteresadoViewSet(viewsets.ModelViewSet):
    serializer_class = COL_InteresadoSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
        
    def list(self,request):
        COL_Interesado_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(COL_Interesado_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Interesado (COL) creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            COL_interesado_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if COL_interesado_serializer.is_valid():
                COL_interesado_serializer.save()
                return Response(COL_interesado_serializer.data, status = status.HTTP_200_OK)
            return Response(COL_interesado_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe Interesado (COL) con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        COL_Interesado = self.get_queryset().filter(id=pk).first()
        if COL_Interesado:
            COL_Interesado.state = False
            COL_Interesado.save()
            return Response({'message':'Interesado (COL) eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Interesado (COL) con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class CR_InteresadoViewSet(viewsets.ModelViewSet):
    serializer_class = CR_InteresadoSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
        
    def list(self,request):
        CR_Interesado_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(CR_Interesado_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Interesado (CR) creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            CR_Interesado_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if CR_Interesado_serializer.is_valid():
                CR_Interesado_serializer.save()
                return Response(CR_Interesado_serializer.data, status=status.HTTP_200_OK)
            return Response(CR_Interesado_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        CR_Interesado = self.get_queryset().filter(id=pk).first()
        if CR_Interesado:
            CR_Interesado.state = False
            CR_Interesado.save()
            return Response({'message':'Interesado (CR) eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Interesado (CR) con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class COL_AgrupacionInteresadosViewSet(viewsets.ModelViewSet):
    serializer_class = COL_AgrupacionInteresadosSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        COL_AgrupacionInteresados_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(COL_AgrupacionInteresados_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':' Agrupación de interesados (COL) creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            COL_AgrupacionInteresados_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if COL_AgrupacionInteresados_serializer.is_valid():
                COL_AgrupacionInteresados_serializer.save()
                return Response(COL_AgrupacionInteresados_serializer.data, status = status.HTTP_200_OK)
            return Response(COL_AgrupacionInteresados_serializer.errors, status = status.HTYP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        COL_AgrupacionesInteresados = self.get_queryset().filter(id=pk).first()
        if COL_AgrupacionesInteresados:
            COL_AgrupacionesInteresados.state = False
            COL_AgrupacionesInteresados.save()
            return Response({'Agrupación de interesados (COL) eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Agrupación de interesados (COL) con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class col_miembrosViewSet(viewsets.ModelViewSet):
    serializer_class = col_miembrosSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        col_miembros_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(col_miembros_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'miembro creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            col_miembros_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if col_miembros_serializer.is_valid():
                col_miembros_serializer.save()
                return Response(col_miembros_serializer.data, status = status.HTTP_200_OK)
            return Response(col_miembros_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        col_miembros = self.get_queryset().filter(id=pk).first()
        if col_miembros:
            col_miembros.state = False
            col_miembros.save()
            return Response({'message':'Miembro eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe miembro con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
class CR_AgrupacionInteresadosViewSet(viewsets.ModelViewSet):
    serializer_class = CR_AgrupacionInteresadosSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        CR_AgrupacionInteresados_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(CR_AgrupacionInteresados_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Agrupación de interesados (CR) creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            CR_AgrupacionInteresados_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if CR_AgrupacionInteresados_serializer.is_valid():
                CR_AgrupacionInteresados_serializer.save()
                return Response(CR_AgrupacionInteresados_serializer.data, status = status.HTTP_200_OK)
            return Response(CR_AgrupacionInteresados_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        CR_AgrupacionInteresados = self.get_queryset().filter(id=pk).first()
        if CR_AgrupacionInteresados:
            CR_AgrupacionInteresados.state = False
            CR_AgrupacionInteresados.save()
            return Response({'message':'Agrupación de interesados (CR) elimianda correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe Agrupacuión de interesados (CR) con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

class LC_InteresadoContactoViewSet(viewsets.ModelViewSet):
    serializer_class = LC_InteresadoContactoSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        LC_InteresadoContacto_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(LC_InteresadoContacto_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'COntacto de interesado creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            LC_InteresadoContacto_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if LC_InteresadoContacto_serializer.is_valid():
                LC_InteresadoContacto_serializer.save()
                return Response(LC_InteresadoContacto_serializer.data, status = status.HTTP_200_OK)
            return Response(LC_InteresadoContacto_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        LC_InteresadoContacto = self.get_queryset().filter(id=pk).first()
        if LC_InteresadoContacto:
            LC_InteresadoContacto.state = False
            LC_InteresadoContacto.save()
            return Response({'message':'Contacto de interesado eliminado correcamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe contacto de interesado con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

