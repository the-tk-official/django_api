from rest_framework import generics

from test_app.models import TestModel
from test_app.serializers import SimpleSerializer

# Create your views here.

class SimpleGenerics(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer

class SimpleGenericsUpdate(generics.UpdateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer
    lookup_field = 'id'