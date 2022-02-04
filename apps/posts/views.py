# Rest framework
from rest_framework.response import Response
from rest_framework import viewsets, status

# jwt
from rest_framework_simplejwt.authentication import JWTAuthentication

# serializers
from .serializer import postsSerializer


# Create your views here.

class postsViewSet(viewsets.ModelViewSet):
    serializer_class = postsSerializer
    
    def get_queryset(self, pk=None):
        if pk:
            return self.get_serializer().Meta.model.objects.filter(user=pk)
        return self.get_serializer().Meta.model.objects.all()

    # get user of token
    def get_user(self,token):
        jwt = JWTAuthentication()
        auth_token = jwt.get_validated_token(token)
        user = jwt.get_user(auth_token)
        return user
    
    # get all posts
    def list(self,request):
        token = request.COOKIES.get('access_token')
        user = self.get_user(token)
        posts_serializer = self.get_serializer(self.get_queryset(user),many=True)
        return Response(posts_serializer.data,status=status.HTTP_200_OK)

    # save a new post
    def create(self,request):
        token = request.COOKIES.get('access_token')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'error':False},status=status.HTTP_201_CREATED)
        return Response({'error':True},status=status.HTTP_400_BAD_REQUEST)
