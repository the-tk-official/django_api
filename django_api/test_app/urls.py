from django.urls import path, include

from rest_framework.routers import DefaultRouter

from test_app.views import SimpleGenerics

router = DefaultRouter()
router.register('simple-viewset', SimpleGenerics)

urlpatterns = [
    path('', include(router.urls))
]
