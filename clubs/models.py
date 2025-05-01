from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_organizer = models.BooleanField(default=False)
    organizer_approved = models.BooleanField(default=False)  # Admin approves organizer manually

    def __str__(self):
        return self.username
    
from django.db import models
from django.conf import settings

class OrganizerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    club_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # add more fields as needed

    def __str__(self):
        return f"{self.user.username} - {self.club_name}"
