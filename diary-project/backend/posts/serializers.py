from rest_framework import serializers
from .models import Article

# 기본 ArticleSeralizer
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        field = "__all__"

    def create(self, validated_data):
        author = self.context['request'].user
        
        article = Article.objects.create(author=author, **validated_data)
        return article