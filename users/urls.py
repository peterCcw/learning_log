"""Defines templates of URL for learning_logs"""
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Adding default url authorization addresses
    path('', include('django.contrib.auth.urls')),
]