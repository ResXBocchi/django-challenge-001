from django.shortcuts import render
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from articles.models import Article
from .serializers import ArticleSerializer
from rest_framework import generics

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filterset_fields = ['category']
