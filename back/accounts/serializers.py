from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

class UserRegisterSerializer(RegisterSerializer):
    birth = serializers.DateField(required=True)

    def custom_signup(self, request, user):
        user.birth = self.validated_data.get('birth')
        user.save()

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['birth'] = self.validated_data.get('birth')
        return data

# 나중에 하기
class CustomUserDetailsSerializer(UserDetailsSerializer):
    # 기존 필드 이외에 추가하고 싶은 필드를 정의합니다.
    birth = serializers.DateField(read_only=True)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = UserDetailsSerializer.Meta.model
        fields = UserDetailsSerializer.Meta.fields + ('birth', 'username')