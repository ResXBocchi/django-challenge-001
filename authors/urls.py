from .views import AuthorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'/api/admin/authors', AuthorViewSet, basename='author')
urlpatterns = router.urls