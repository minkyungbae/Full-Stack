from rest_framework import generics, status
from .serializers import UserSignUpSerializer, UserLogInSerializer, UserLogOutSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

# 회원 가입
class UserSignUpView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer


# 로그인
class LogInView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny] # 인증되지 않은 사람도 접근 가능
    serializer_class = UserLogInSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh' : str(refresh),
            'access' : str(refresh.access_token)
        }, status=status.HTTP_200_OK)
        
    
# 로그아웃
class LogOutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserLogOutSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            refresh_token = serializer.validated_data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)