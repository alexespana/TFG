# myFindings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.index, name='home'),
    # Sobre la aplicación
    path('about/', views.about, name='about'),
    # Contacto
    path('contact/', views.contact, name='contact'),
    # Equipo
    path('team/', views.team, name='team'),
]