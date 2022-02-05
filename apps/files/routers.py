# Routes for files
from rest_framework.routers import DefaultRouter

# Viewsets
from apps.files.views import FilesViewset

router = DefaultRouter()  # Instance of DefaulRouter

router.register(r'files',FilesViewset,basename='files')

urlpatterns = router.urls