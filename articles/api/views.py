from django.shortcuts import render
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from articles.models import Article
from .serializers import ArticleSerializer, ArticleAdminSerializer
from rest_framework import generics,permissions

class ArticleAdminViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleAdminSerializer
    permission_classes = (permissions.IsAdminUser,)
    filterset_fields = ['category']

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filterset_fields = ['category']
