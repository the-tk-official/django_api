from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import CustomUserView, UserProfileView

router = DefaultRouter()
router.register('user', CustomUserView)
router.register('user-profile', UserProfileView)

urlpatterns = [
    path('', include(router.urls))
]