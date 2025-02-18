from rest_framework import serializers
from .models import Article

# 기본 ArticleSeralizer
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        field = "__all__"
        read_only_fields = ('author',)
        exclude = ("created_date", "updated_date")