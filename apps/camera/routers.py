# Routes for camera
from rest_framework.routers import DefaultRouter

# Viewsets
from apps.camera.views import CameraViewset

router = DefaultRouter()  # Instance of DefaulRouter

router.register(r'pictures',CameraViewset,basename='pictures')

urlpatterns = router.urls