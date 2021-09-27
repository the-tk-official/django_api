from django.contrib import admin

from event_controller.models import EventAttender, EventFeature, EventMain

# Register your models here.

admin.site.register((EventAttender, EventFeature, EventMain))
