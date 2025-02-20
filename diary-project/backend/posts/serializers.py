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
    
# Update serializer
class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        field = ["title", "content"]
        read_only_fields = ("id","author",)
        exclude = ("created_date", "updated_date")
        
    def valiate(self, data):
        instance = self.instance
        request = self.context.get('request')
        if request and request.user != instance.author:
            raise serializers.ValidationError("글 작성자가 아니시군요?? 글 작성자만 수정 가능합니다.")
        return data
    
    def update(self, instance, validated_data):
        """title update, 기본값은 본래의 title"""
        instance.title = validated_data.get('title', instance.title)
        """content update, 기본값은 본래의 content"""
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
        

# Delete serializer
class ArticleDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        
    def validate(self, data):
        instance = self.instance
        request = self.context.get('request')
        if request and request.user != instance.author:
            raise serializers.ValidationError("글 작성자도 아니면서 왜 삭제하려 하세욧?")
        return data
    
    def delete(self, instance):
        instance.delete()