from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Article
from .serializers import ArticleSerializer

# 글 목록 불러오기
class ArticleListView(generics.ListAPIView):
    permission_classes = [AllowAny] # 누구든지 접근 가능
    
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

# 글 생성하기
class ArticleCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer
    
    def perform_create(self, serializer):
        serializer.save() # serializer.create() 로 변경 (validated_data는 serializer에서 처리)