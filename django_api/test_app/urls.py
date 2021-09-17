from django.urls import path

from test_app.views import simple

urlpatterns = [
    path('simple/', simple)
]
