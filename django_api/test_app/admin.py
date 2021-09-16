from django.contrib import admin

from test_app.models import TestModel, ModelX, ModelY

# Register your models here.

admin.site.register((TestModel, ModelX, ModelY))
