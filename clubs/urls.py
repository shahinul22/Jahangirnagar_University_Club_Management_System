from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL -> home page
    path('register/organizer/', views.register_organizer, name='register_organizer'),
    path('register/user/', views.register_regular, name='register_regular'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
