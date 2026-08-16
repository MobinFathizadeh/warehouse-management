from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .services import authenticate_user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate_user(data['username'], data['password'])
        if user is None:
            raise serializers.ValidationError('نام کاربری یا رمز عبور اشتباه است')
        data['user'] = user
        return data