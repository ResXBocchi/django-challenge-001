"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from authors.api.views import AuthorAdminViewSet
from articles.api.views import ArticleViewSet, ArticleAdminViewSet
from users.api.views import FacebookLogin, TwitterLogin,FacebookConnect,TwitterConnect
from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)
from django.conf.urls.static import static
from news import settings


router = routers.SimpleRouter()
router.register(r'api/articles', ArticleViewSet, 'Article')
router.register(r'api/admin/articles', ArticleAdminViewSet, basename='adm_article')
router.register(r'api/admin/authors', AuthorAdminViewSet, basename='adm_author')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include('rest_auth.urls')),
    url(r'^api/signup', include('rest_auth.registration.urls')),
    url(r'^api/login/facebook', FacebookLogin.as_view(), name='fb_login'),
    url(r'^api/login/twitter', TwitterLogin.as_view(), name='twitter_login'),
    url(r'^api/connect/facebook', FacebookConnect.as_view(), name='fb_connect'),
    url(r'^api/connect/twitter', TwitterConnect.as_view(), name='twitter_connect'),
    url(r'^socialaccounts', SocialAccountListView.as_view(), name='social_account_list'),
    url(
        r'^socialaccounts/(?P<pk>\d+)/disconnect',
        SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'
    )
]
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

