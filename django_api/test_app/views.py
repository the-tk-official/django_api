from django.shortcuts import render
from django.http import JsonResponse, response
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

from test_app.models import TestModel
from test_app.serializers import SimpleSerializer

# Create your views here.

class Simple(APIView):

    def post(self, request):
        serializer = SimpleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_test_content = TestModel.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            phone_number=request.data['phone_number'],
            is_alive=request.data['is_alive'],
            amount=request.data['amount']
        )

        return JsonResponse({'data': SimpleSerializer(new_test_content).data})

    def get(self, request):
        content = TestModel.objects.all().values()
        return JsonResponse({'data': SimpleSerializer(content).data})

