from django.shortcuts import render
from rest_framework import viewsets
from authors.models import Author
from .serializers import AuthorSerializer
# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()