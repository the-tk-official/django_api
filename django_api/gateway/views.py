from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework.views import APIView, Response

import jwt
import random
import string
from datetime import datetime, timedelta

from user.models import CustomUser
from gateway.models import Jwt
from gateway.serializers import LoginSerializer, RegisterSerializer

# Create your views here.

def get_random(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def get_access_token(payload):
    return jwt.encode(
        {'exp': datetime.now() + timedelta(minutes=5), **payload},
        settings.SECRET_KEY,
        algorithm='HS256'
    )


def get_refresh_token():
    return jwt.encode(
        {'exp': datetime.now() + timedelta(days=365), "data": get_random(length=10)},
        settings.SECRET_KEY,
        algorithm='HS256'
    )


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        if not user:
            return Response({'error': 'Invalid email or password'}, status='400')

        access = get_access_token({'user_id': user.id})
        refresh = get_refresh_token()

        Jwt.objects.create(
            user_id=user.id,
            access=access,
            refresh=refresh
        )

        return Response({
            'access': access,
             'refresh': refresh
        })


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        CustomUser.objects._create_user(**serializer.validated_data)

        return Response({'success': 'User created.'})
