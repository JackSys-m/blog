from django.shortcuts import render

def index(request):
    """Домашняя страница приложения Blogs."""
    return render(request, 'blogs/index.html')
