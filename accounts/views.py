from django.contrib.admin import action
from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import mixins, viewsets
from .models import User, Role, Permission, RolePermission

from .serializers import LoginSerializer, LogoutSerializer, UserSerializer, RoleSerializer, PermissionSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user':{
                    'id':user.id,
                    'username':user.username,
                    'first_name':user.first_name,
                    'last_name':user.last_name,
                    'role':user.role.name,
                }
            }
        )



class LogoutView(APIView):
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'با موفقیت خارج شدید'})



class UserViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


    @action(detail=True, methods=['post'])
    def permissions(self, request, pk=None):
        role = self.get_object()
        permission_id = request.data.get('permission_id')

        if RolePermission.objects.filter(role=role, permission_id=permission_id).exists():
            return Response({'error': 'already_exists', 'message': 'این مجوز قبلاً تخصیص داده شده است'}, status=409)

        role_permission = RolePermission.objects.create(role=role, permission_id=permission_id)
        return Response({'id': role_permission.id, 'role': role.id, 'permission': permission_id}, status=201)


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer