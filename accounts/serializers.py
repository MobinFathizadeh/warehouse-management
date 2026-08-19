from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

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

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate_refresh_token(self, value):
        try:
            RefreshToken(value)
        except TokenError:
            raise serializers.ValidationError("توکن نا معتبر است")
        return value

    def save(self):
        token = RefreshToken(self.validated_data['refresh_token'])
        token.blacklist()