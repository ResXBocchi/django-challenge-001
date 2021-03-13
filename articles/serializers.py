from rest_framework import serializers
from users.serializers import UserDetailsSerializer
from .models import Article, Category
from news import settings


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')

class CategoryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)

class ArticleSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(source='uuid')
    author = UserDetailsSerializer()
    category = serializers.SlugField(source='category.title')

    class Meta:
        model = Article
        exclude=('created_at','updated_at','uuid')
        depth = 1


    def create(self, validated_data):
        category = validated_data.pop('category')
        category_instance, created = Category.objects.get_or_create(name=category)
        article_instance = Article.objects.create(**validated_data, category=category_instance)
        return article_instance

