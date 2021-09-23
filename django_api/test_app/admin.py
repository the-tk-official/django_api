from django.contrib import admin

from test_app.models import TestModel, ModelX, ModelY, Blog, Car

# Register your models here.

admin.site.register((Blog, Car,TestModel, ModelX, ModelY))
