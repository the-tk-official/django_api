"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include(('test_app.urls', 'test_app'), namespace='test')),
    path('gateway/', include(('gateway.urls', 'gateway'), namespace='gateway')),
    path('user-main/', include(('user.urls', 'user'), namespace='user')),
]

# Include debug_toolbar
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
