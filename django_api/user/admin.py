from django.contrib import admin

from user.models import CustomUser, UserProfile

# Register your models here.

admin.site.register((CustomUser, UserProfile))
