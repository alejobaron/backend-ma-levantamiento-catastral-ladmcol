from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.users.models import User
from apps.users.api.access_policies import UserAccessPolicy
from apps.users.api.serializers import UserSerializer, UserListSerializer, UpdateUseSerializer, PasswordSerializer

class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    queryset = None
    access_policy = UserAccessPolicy()

    def get_object(self, pk):
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk)
        
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.serializer_class().Meta.model.objects.filter(is_active =True).values('id','username','email','name')
        return self.queryset
    
    @action(detail=True, methods=['post'])
    def set_password(self,request, pk=None):
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({'message':'Contraseña actualizada correctamente.'})
        return Response({'message':'Hay errores en la información enviada.',
                         'errors':password_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        user = self.get_queryset()
        user_serializer = self.list_serializer_class(user, many = True)
        return Response(user_serializer.data, status = status.HTTP_200_OK)
    
    def create (self, request):
        user_serializer = self.serializer_class(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Usuario registrado correctamente'}, status = status.HTTP_200_OK)
        return Response({
            'message':'Errores en el registro.', 'errors': user_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        
    def retrieve (self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response (user_serializer.data)
    
    def update (self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUseSerializer(user, data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Usuario actualizado correctamente'}, status=status.HTTP_200_OK)
        return Response({'message':'Hay errores en la actualización.','errors': user_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk = None):
        user = self.get_object(pk)
        if user.is_active:
            user.is_active = False
            user.save()
            return Response({'message':'Usuario eliminado correctamente.'})
        return Response({'message':'No existe el usuario que se desea eliminar'}, status = status.HTTP_404_NOT_FOUND)