# Generated by Django 5.2 on 2025-05-01 15:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clubs", "0002_remove_customuser_is_regular_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_regular_user",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="OrganizerProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("club_name", models.CharField(max_length=100)),
                ("club_description", models.TextField()),
                ("contact_person_name", models.CharField(max_length=100)),
                ("contact_email", models.EmailField(max_length=254)),
                ("contact_phone", models.CharField(max_length=15)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organizer_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
