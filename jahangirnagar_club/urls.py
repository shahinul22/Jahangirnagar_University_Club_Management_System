from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clubs.urls')),  # Now everything from clubs app will be routed from here
]