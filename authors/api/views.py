from django.shortcuts import render
from rest_framework import viewsets,permissions
from authors.models import Author
from .serializers import AuthorSerializer
# Create your views here.

class AuthorAdminViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = (permissions.IsAdminUser,)