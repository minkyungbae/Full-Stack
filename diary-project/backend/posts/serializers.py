from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Post

# 글쓰기
class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        field = "__all__"
        