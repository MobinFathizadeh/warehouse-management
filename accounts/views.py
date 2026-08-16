from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'user':{
                    'id':user.id,
                    'username':user.username,
                    'first_name':user.first_name,
                    'last_name':user.last_name,
                    'role':user.role.name,
                }
            }
        )

