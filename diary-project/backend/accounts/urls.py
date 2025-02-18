from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name="signup"), # 회원가입만 구현
    path('login/', views.LogInView.as_view(), name="login"), # 로그인
    path('logout/', views.LogOutView.as_view(), name="logout") # 로그아웃
]
