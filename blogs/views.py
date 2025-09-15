from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogForm, EntryForm

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

def new_blog(request):
    """Определяет новый блог."""
    if request.method != 'POST':
        # Данные не отправлялись; создаётся пустая форма
        form = BlogForm()
    else:
        # Отправлены данные POST: обработать данные
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')

    # Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

def new_entry(request, blog_id):
    """Добавляет новую запись по конкретному блогу."""
    blog = BlogPost.objects.get(id=blog_id)
    if request.method != 'POST':
        # Данные не отправлялись; создаётся пустая форма
        form = EntryForm()
    else:
        # Отправлены данные POST: обработать данные
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.blog = blog
            new_entry.save()
            return redirect('blogs:blogs', blog_id=blog_id)
    # Вывести пустую или недействительную форму
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_blog.html', context)