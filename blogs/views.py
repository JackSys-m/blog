from django.shortcuts import render
from .models import BlogPost

def index(request):
    """Домашняя страница приложения Blogs."""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Выводит перечень блогов."""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """Выводит один блог и все записи."""
    blog = BlogPost.objects.get(id=blog_id)
    entries = blog.entry_set.order_by('date_added')
    context = {'blog': blog, 'entries': entries}
    return render(request, 'blogs/blog.html', context)