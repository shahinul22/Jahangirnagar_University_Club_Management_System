from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, OrganizerProfile

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created and instance.is_organizer:
        OrganizerProfile.objects.get_or_create(user=instance)
