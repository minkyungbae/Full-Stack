from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="post-list"), # 글 목록 가기
]
