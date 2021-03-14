from .views import ArticleViewSet, ArticleList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'/api/admin/articles', ArticleViewSet, basename='adm_article')
router.register(r'/api/articles/', ArticleList, basename='article')
urlpatterns = router.urls