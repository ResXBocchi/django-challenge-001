from rest_framework import serializers
from authors.serializers import AuthorSerializer
from .models import Article
from news import settings


class ArticleSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()

    class Meta:
        model = Article
        exclude=('created_at','updated_at')
        depth = 1
