from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_organizer = models.BooleanField(default=False)
    is_regular_user = models.BooleanField(default=True)

    def __str__(self):
        return self.username

