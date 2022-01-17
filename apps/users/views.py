# rest framework
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import viewsets

# DJango
from django.contrib.auth import authenticate
from django.conf import settings

# simple JWT
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


# serializers
from apps.users.serializer import UserSerializer,CustomTokenObtainPairSerializer, LogoutSerializer

# register
class Register(GenericAPIView):
    serializer_class = UserSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)  # get data 
        if serializer.is_valid():
            serializer.save()
            return Response({'error':False, 'message':'Usuario creado con exito'},status=status.HTTP_201_CREATED)
        return Response({'error':True, 'message':serializer.errors },status=status.HTTP_400_BAD_REQUEST)

# login
class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self,request,*args,**kwargs):
        response = Response()

        # get credentials 
        username = request.data.get('username','')  # if not credentials, set null
        password = request.data.get('password','')
        user = authenticate(username=username,password=password)  # search user

        if user:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user_serializer = UserSerializer(user)  # get user
                # cookie
                response.set_cookie(
                    key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                    value = serializer.validated_data.get('access'),
                    expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                # return data
                response.data = {
                    'refresh_token':serializer.validated_data.get('refresh'),
                    'user':user_serializer.data,
                    'error':False
                    }
                return response

# logout
class LogoutAPIView(GenericAPIView):
    serializer_class = LogoutSerializer

    def get(self,request):
        response = Response()
        response.delete_cookie('access_token')
        response.data = {'message':'Session cerrada correctamente.'}
        return response

# Update token
class RefreshTokenView(TokenViewBase):
    serializer_class = serializers.TokenRefreshSerializer

    # Sobreescribo el metodo post de TokenViewBase
    def post(self, request, *args, **kwargs):
        response = Response()
        serializer = self.get_serializer(data=request.data)
        # Si actualiza el token, que actualize la cookie
        try:
            serializer.is_valid(raise_exception=True)
            response.set_cookie('access_token',serializer.validated_data['access'])
            response.data = {'refresh_token': serializer.validated_data['refresh'],'message':'Token actualizado.'}
        except TokenError as e:
            response.data = {'error':True}
            raise InvalidToken(e.args[0])

        return response


