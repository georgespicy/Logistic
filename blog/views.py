from django.shortcuts import render
from .models import Category, Post

def blog(request):
    categories = Category.objects.all()[:6]
    posts = Post.objects.all()
    context = {
        'categories': categories,
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    categories = Category.objects.all()[:6]
    context = {
        'categories': categories,
        'post': post,
        
    }
    return render(request, 'blog/blog_detail.html', context)