from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserRegisterView.as_view(), name="register"), # 회원가입만 구현
]
