from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from user.models import CustomUser, UserProfile
from user.serializers import CustomUserSerializer, UserProfileSerializer

# Create your views here.

class CustomUserView(ModelViewSet):

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.prefetch_related('user_profile', 'user_profile__address_info')


class UserProfileView(ModelViewSet):

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.select_related('user', 'address_info')
