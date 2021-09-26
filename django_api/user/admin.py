from django.contrib import admin

from user.models import AddressGlobal, CustomUser, UserProfile

# Register your models here.

admin.site.register((AddressGlobal, CustomUser, UserProfile))
