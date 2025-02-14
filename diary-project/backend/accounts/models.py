from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 원하는 필드를 추가
    nickname = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

    # 객체의 문자열 표현 정리 : User를 view에서 쓸 때 username이 return 됨
    def __str__(self):
        return self.username