from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name="articlelist"), # 글 목록 가기
]
