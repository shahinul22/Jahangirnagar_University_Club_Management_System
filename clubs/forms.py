from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

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
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_organizer = False
        user.is_regular_user = True
        if commit:
            user.save()
        return user
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

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
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_organizer = False
        user.is_regular_user = True
        if commit:
            user.save()
        return user
