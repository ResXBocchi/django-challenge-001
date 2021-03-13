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
from django.urls import path
from django.conf.urls import url, include
from articles import views
from rest_framework import routers
from users.views import UserViewSet
from articles.views import ArticleViewSet

router = routers.SimpleRouter()
router.register(r'api/users', UserViewSet, 'User')
router.register(r'api/articles', ArticleViewSet, 'Article')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/', include('knox.urls'))
]
urlpatterns += router.urls