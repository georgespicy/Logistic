from django.shortcuts import render
from .models import Category

def blog(request):
    categories = Category.objects.all()[:6]
    context = {
        'categories': categories
    }
    return render(request, 'blog/blog.html', context)

def blog_detail(request):
    return render(request, 'blog/blog_detail.html')