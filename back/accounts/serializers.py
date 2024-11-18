from dj_rest_auth.registration.serializers import RegisterSerializer
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


