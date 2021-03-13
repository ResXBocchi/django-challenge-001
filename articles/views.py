from django.shortcuts import render
from rest_framework import viewsets
from .models import Article, Category
from .serializers import ArticleSerializer
import django_filters.rest_framework

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    