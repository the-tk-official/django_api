from django.urls import path, include
from rest_framework.routers import DefaultRouter

from event_controller.views import EventMainView, EventAttenderView

router = DefaultRouter()
router.register('event-attender', EventAttenderView)
router.register('event', EventMainView)

urlpatterns = [
    path('', include(router.urls)),
]
