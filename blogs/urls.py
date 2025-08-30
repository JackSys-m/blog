"""Определяет схемы URL для blogs."""
from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
]
