# vendors/urls.py
from django.urls import path
from . import views

app_name = 'vendors'

urlpatterns = [
    # Add this line to handle the base /vendors/ URL
    # You can point it to an existing view like 'dashboard' or a new one.
    path('', views.dashboard, name='dashboard_root'), # Option 1: point to existing dashboard
    # OR: path('', views.vendor_home, name='vendor_home'), # Option 2: point to a new specific home view

    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
]