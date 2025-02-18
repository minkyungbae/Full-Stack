from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Article

# 글쓰기
class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        field = "__all__"
        