from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

# settings.py에 선언했던 AUTH_USER_MODEL을 데려옴
User = get_user_model()

# 회원 가입
class UserSignUpSerializer(serializers.ModelSerializer):
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
    
# 로그인    
class UserLogInSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True) # 필수 입력
    password = serializers.CharField(required=True, write_only=True) # 필수 입력
    
    class Meta:
        model = User
        fields = ('username', 'nickname', 'password', 'password2', 'bio',)
    
    def validate_Userpassword(self, password):
        if not str() in password:
            raise ValidationError("비밀번호에 문자는 필수입니다.")
        if not int() in password:
            raise ValidationError("비밀번호에 숫자는 필수입니다.")
        return password
    
    def validate_Username(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise ValidationError("아이디 또는 비밀번호가 일치하지 않습니다.")
        data['user']=user
        return data 