
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class OrganizerRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_organizer = True
        user.is_regular_user = False
        if commit:
            user.save()
        return user


class RegularUserRegisterForm(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@juniv.edu'):
            raise ValidationError('Please use your university email (e.g., yourname@juniv.edu)')
        return email
