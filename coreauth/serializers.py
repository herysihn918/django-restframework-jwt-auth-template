from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
# from django.contrib.auth.models import User
from .models import User


class UserSerializer(serializers.ModelSerializer):
    user_role = serializers.SerializerMethodField()

    def get_user_role(self, obj):
        return obj.get_user_role_display()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'company_name', 'user_role', 'id')

class UserSerializerForRegister(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'company_name', 'user_role', 'id', 'password')

class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    user_role = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def get_user_role(self, obj):
        return obj.get_user_role_display()

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'first_name', 'last_name', 'email', 'company_name', 'user_role', 'id')