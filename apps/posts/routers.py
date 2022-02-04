# Routes for posts
from rest_framework.routers import DefaultRouter

# Viewsets
from apps.posts.views import postsViewSet

router = DefaultRouter()  # Instance of DefaulRouter

router.register(r'posts',postsViewSet,basename='posts')

urlpatterns = router.urls