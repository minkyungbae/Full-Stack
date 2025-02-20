from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name="articlelist"), # 글 목록 가기
    path('create/', views.ArticleCreateView.as_view(), name="create"), # 글 생성
    path('update/<int:pk>/', views.ArticleUpdateView.as_view(), name="update"), # 글 수정
    path('delete/<int:pk>/', views.ArticleDeleteView.as_view(), name="delete"), # 글 삭제
    
]
