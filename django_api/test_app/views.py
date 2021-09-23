from rest_framework import viewsets

from test_app.models import TestModel, Car
from test_app.serializers import SimpleSerializer

from django_seed import Seed

from random import randint

from test_app.models import Blog

# Create your views here.

car_names = ('Nissan', 'Toyota', 'Mazda', 'Doodge', 'Honda',)

seeder = Seed.seeder()

seeder.add_entity(Car, 100, {
    'name': lambda x: car_names[randint(0, len(car_names) - 1)]
})

def execute():
    seeder.execute()
    print('Seeding Completed')


class SimpleGenerics(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer
