from rest_framework import serializers
from .models import Article

# 기본 ArticleSeralizer
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        field = "__all__"
        read_only_fields = ('author',)
        exclude = ("created_date", "updated_date")
        
    def create(self, validated_data):
        author = self.context['request'].user
        validated_data['author'] = author # validated_data 에 author 추가
        return super().create(validated_data) # super().create() 호출