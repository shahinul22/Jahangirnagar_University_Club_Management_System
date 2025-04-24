from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_organizer = models.BooleanField(default=False)
    organizer_approved = models.BooleanField(default=False)  # Admin approves organizer manually

    def __str__(self):
        return self.username
