from django.urls import path

from test_app.views import SimpleGenerics, SimpleGenericsUpdate

urlpatterns = [
    path('simple-generics/', SimpleGenerics.as_view()),
    path('simple-generics/<int:id>/', SimpleGenericsUpdate.as_view()),
]
