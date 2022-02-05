# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# rest framework
from rest_framework import permissions
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny


# Simple JWT
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

# views
from apps.users.views import Login, LogoutAPIView, Register

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('login/',Login.as_view(),name='login'),
    path('logout/',LogoutAPIView.as_view(),name='logout'),
    path('camera/',include('apps.camera.routers')),
    path('storage/',include('apps.files.routers')),
    path('posts/',include('apps.posts.routers')),
    path('register/',authentication_classes([])(permission_classes([AllowAny])(Register)).as_view(),name='register'),
]

# Static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
