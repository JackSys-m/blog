"""Определяет схемы URL для blogs."""
from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех блогов
    path('blogs/', views.blogs, name='blogs'),
    # Страница с подробной информацией по отдельному блогу
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    path('new_blog/', views.new_blog, name='new_blog'),
    # Страница для добавления новой записи
    path('new_entry/<int:blog_id>', views.new_entry, name='new_entry'),
]
