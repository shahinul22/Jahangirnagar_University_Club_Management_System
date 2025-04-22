from django.contrib.auth.views import LogoutView  # Import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.login_view, name='home'),  # Root URL redirects to login page
    path('register/organizer/', views.register_organizer, name='register_organizer'),
    path('register/user/', views.register_regular, name='register_regular'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
]
