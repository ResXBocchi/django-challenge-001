from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'/api/articles', ArticleViewSet, basename='article')
urlpatterns = router.urls