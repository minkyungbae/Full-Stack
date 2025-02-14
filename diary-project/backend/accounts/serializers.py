from rest_framework import serializers
from django.contrib.auth import get_user_model

# settings.py에 선언했던 AUTH_USER_MODEL을 데려옴
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True) # 비밀번호 확인 / 필수 요소

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'nickname', 'bio')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    # 검증 단계
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다.")
        return attrs

    # 생성 단계
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user