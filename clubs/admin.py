from django.contrib import admin

# Register your models here.

from .models import CustomUser, OrganizerProfile

admin.site.register(CustomUser),
admin.site.register(OrganizerProfile)