# Rest framework
from rest_framework.response import Response
from rest_framework import viewsets, status

# Simple JWT
from rest_framework_simplejwt.authentication import JWTAuthentication

# serializer
from apps.files.serializers import FilesSerializer

class FilesViewset(viewsets.GenericViewSet):
    serializer_class = FilesSerializer

    # query
    def get_queryset(self,pk=None):
        if pk:
            return self.serializer_class.Meta.model.objects.filter(user=pk)
        return self.serializer_class.Meta.model.objects.all()

    # get user of token
    def get_user(self,token):
        jwt = JWTAuthentication()
        auth_token = jwt.get_validated_token(token)
        user = jwt.get_user(auth_token)
        return user

    # get all files
    def list(self,request):
        token = request.COOKIES.get('access_token')
        user = self.get_user(token)
        files_serializer = self.serializer_class(self.get_queryset(user),many=True)
        return Response(files_serializer.data,status=status.HTTP_200_OK)

    # save new file   
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'error':False},status=status.HTTP_201_CREATED)
        return Response({'error':True},status=status.HTTP_400_BAD_REQUEST)
    
    # delete a file
    def destroy(self,request,pk=None):
        file = self.get_queryset().filter(id=pk)
        if file:
            file.delete()
            return Response({'error':False},status=status.HTTP_200_OK)
        return Response({'error':True},status=status.HTTP_400_BAD_REQUEST)