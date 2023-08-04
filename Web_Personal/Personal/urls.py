from .views import inicio
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', inicio, name="Inicio"),
]
