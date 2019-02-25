from django.shortcuts import render, get_object_or_404, redirect
from .forms import BlogForm
from .models import Blog

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'blog':blog})

def blog_create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, 'blog_form.html', {'form':form})

def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog_form.html', {'form': form})

def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request, 'blog_delete.html', {'object': blog})