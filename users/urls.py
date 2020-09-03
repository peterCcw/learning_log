"""Defines templates of URL for users"""
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Adding default url authorization addresses
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
]