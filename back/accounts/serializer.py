from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    birth = serializers.DateField()
    def save(self, request):
        user = super().save(request)
        user.date_of_birth = self.data.get('birth')
        user.save()
        return user