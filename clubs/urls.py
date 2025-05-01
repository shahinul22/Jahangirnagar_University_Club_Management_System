from django.urls import path
from . import views

urlpatterns = [
    # Public views
    path('', views.home, name='home'),
    path('register/organizer/', views.register_organizer, name='register_organizer'),
    path('register/regular/', views.register_regular, name='register_regular'),

    # Login views
    path('login/admin/', views.admin_login, name='admin_login'),
    path('login/organizer/', views.organizer_login, name='organizer_login'),
    path('login/user/', views.user_login, name='user_login'),

    # Logged-in user views
    path('dashboard/', views.dashboard, name='dashboard'),
    path('organizer/dashboard/', views.organizer_dashboard, name='organizer_dashboard'),

    # Admin views (no `/admin/` prefix here)
    path('admin-panel/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/pending_organizers/', views.pending_organizers, name='pending_organizers'),
    path('admin-panel/approve_organizer/<int:user_id>/', views.approve_organizer, name='approve_organizer'),

    # Logout view
    path('logout/', views.logout_view, name='logout'),

    # Make sure to define the login URL if it's not already defined
    path('login/', views.user_login, name='login'),  # Add this line
]