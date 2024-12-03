from django.shortcuts import render
from django.contrib.auth import get_user_model
from accounts.serializers import CustomUserDetailsSerializer 
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.response import Response
from .models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    if request.method=='GET':
        user = User.objects.get(pk=request.user.id)
        serializer = CustomUserDetailsSerializer(user)
        print(serializer.data)
        return Response(serializer.data)