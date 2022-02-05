# rest framework
from rest_framework import serializers

# simple jwt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# model
from apps.users.models import User

# Add claims to token
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['user_id'] = user.id

        return token

# serializer for users
class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ('id','username','password','email')

    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Encrypt password
        user.save()
        return user

    def update(self,instance,validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

# logout serializer
class LogoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)