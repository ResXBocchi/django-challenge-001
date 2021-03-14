from django.shortcuts import render
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics

class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['category']
