from django.shortcuts import render, get_object_or_404
from .models import BlogPost, BlogCategory

def blog_list(request):
    posts = BlogPost.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'blog/blog_detail.html', {'post': post})
