from django.shortcuts import (
    render, 
    redirect, 
    get_object_or_404
)
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import OrganizerRegisterForm, RegularUserRegisterForm

CustomUser = get_user_model()

# =========================
# Public Views (No Login)
# =========================

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'clubs/home.html')


def register_organizer(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = OrganizerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_organizer = True
            user.organizer_approved = False
            user.save()
            messages.info(request, 'Your request has been submitted. Wait for admin approval.')
            return redirect('home')
    else:
        form = OrganizerRegisterForm()

    return render(request, 'clubs/register_organizer.html', {'form': form})


from .forms import RegularUserRegisterForm

def register_regular(request):
    if request.method == 'POST':
        form = RegularUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_regular_user = True  # or whatever flag you use
            user.save()
            login(request, user)
            return redirect('regular_dashboard')  # adjust redirect
    else:
        form = RegularUserRegisterForm()
    return render(request, 'clubs/register_regular.html', {'form': form})


# =========================
# Login Views
# =========================

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')  # Updated path to admin-panel/dashboard/
            else:
                messages.error(request, "You do not have permission to access this page.")
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = AuthenticationForm()

    return render(request, 'clubs/admin_login.html', {'form': form})


def organizer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_organizer and user.organizer_approved:
                login(request, user)
                return redirect('organizer_dashboard')
            else:
                messages.error(request, "You do not have permission to access this page.")
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = AuthenticationForm()

    return render(request, 'clubs/organizer_login.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = AuthenticationForm()

    return render(request, 'clubs/user_login.html', {'form': form})


# =========================
# Logged-In User Views
# =========================

@login_required
def dashboard(request):
    if request.user.is_organizer and request.user.organizer_approved:
        return redirect('organizer_dashboard')
    return render(request, 'clubs/dashboard.html')


@login_required
def organizer_dashboard(request):
    if not request.user.is_organizer or not request.user.organizer_approved:
        return HttpResponseForbidden("You are not approved as an organizer.")
    return render(request, 'clubs/organizer_dashboard.html')


# =========================
# Admin Views
# =========================
User = get_user_model()

@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    # Fetch the updated list of pending organizers
    pending = User.objects.filter(is_organizer=True, organizer_approved=False)
    return render(request, 'clubs/admin_dashboard.html', {'pending': pending})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def pending_organizers(request):
    pending = CustomUser.objects.filter(is_organizer=True, organizer_approved=False)
    return render(request, 'clubs/pending_organizers.html', {'pending': pending})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def approve_organizer(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id, is_organizer=True, organizer_approved=False)
    user.organizer_approved = True
    user.save()
    messages.success(request, f"{user.username} has been approved as an organizer.")
    return redirect('pending_organizers')  # This will redirect to the 'pending_organizers' view

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to a login view that exists in your urls.py