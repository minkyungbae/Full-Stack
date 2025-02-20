from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Article
from .serializers import ArticleSerializer, ArticleUpdateSerializer, ArticleDeleteSerializer

# 글 목록 불러오기
class ArticleListView(generics.ListAPIView):
    permission_classes = [AllowAny] # 누구든지 접근 가능
    
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

# 글 생성하기
class ArticleCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated] # 토큰과 관련된 자격, @login_required는 로그인!
    serializer_class = ArticleSerializer
    
    def perform_create(self, serializer):
        serializer.save() # serializer.create() 로 변경 (validated_data는 serializer에서 처리)

# 글 수정하기
class ArticleUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleUpdateSerializer
    
    def get_serializer_context(self):
        return {'request': self.request }
    
# 글 삭제하기
class ArticleDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleDeleteSerializer
    queryset = Article.objects.all()
    
    def get_serializer_context(self):
        return {'request': self.request }
    
    def perform_destroy(self, instance):
        serializer = self.get_serializer(instance=instance, data={})
        serializer.is_valid()
        serializer.delete(instance)
    