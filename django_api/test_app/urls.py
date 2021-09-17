from django.urls import path

from test_app.views import Simple

urlpatterns = [
    path('simple/', Simple.as_view()),
    path('simple/<int:id>/', Simple.as_view())
]
