from django.urls import path

from gateway.views import LoginView, RegisterView, RefreshView, TestException

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('refresh/', RefreshView.as_view(), name='refresh'),
    path('test-exc/', TestException.as_view()),
]
