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
        serializer.save()
        return JsonResponse({'data': serializer.data})

    def get(self, request):
        content = TestModel.objects.all().values()
        return JsonResponse({'data': SimpleSerializer(content, many=True).data})

    def put(self, request, *args, **kwargs):
        model_id = kwargs.get('id', None)

        if not model_id:
            return JsonResponse({'error': 'method /PUT/ not allowed'})

        try:
            instance = TestModel.objects.get(id=model_id)
        except:
            return JsonResponse({'error': 'Object does not exist'})

        serializer = SimpleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({'data': serializer.data})
