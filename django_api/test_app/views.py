from rest_framework import viewsets

from test_app.models import TestModel
from test_app.serializers import SimpleSerializer

# Create your views here.

class SimpleGenerics(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer
