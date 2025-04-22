from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import OrganizerRegisterForm, RegularUserRegisterForm


# Home View - Redirects to the login page if user is not logged in
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # If user is already logged in, send them to the dashboard
    return render(request, 'clubs/home.html')  # Render the home page for non-authenticated users


# Organizer Registration View
def register_organizer(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # If the user is logged in, redirect them to the dashboard
    
    if request.method == 'POST':
        form = OrganizerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect('dashboard')  # Redirect to dashboard after registration
    else:
        form = OrganizerRegisterForm()
    
    return render(request, 'clubs/register_organizer.html', {'form': form})


# Regular User Registration View
def register_regular(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # If the user is logged in, redirect them to the dashboard
    
    if request.method == 'POST':
        form = RegularUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect('dashboard')  # Redirect to dashboard after registration
    else:
        form = RegularUserRegisterForm()
    
    return render(request, 'clubs/register_regular.html', {'form': form})


# Login View - Redirects to dashboard if user is already logged in
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # If the user is already logged in, redirect them to the dashboard
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log in the user after successful authentication
            return redirect('dashboard')  # Redirect to the dashboard after logging in
    else:
        form = AuthenticationForm()
    
    return render(request, 'clubs/login.html', {'form': form})


# Dashboard View - This is where the logged-in user is redirected after login
@login_required
def dashboard(request):
    return render(request, 'clubs/dashboard.html')  # Render the dashboard page for authenticated users
