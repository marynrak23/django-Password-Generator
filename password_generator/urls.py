"""password_generator URL Configuration
    Main Urls
"""
from django.urls import path
from generator import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generated_password', views.password, name='password'),
    path('about', views.about, name='about'),
]
