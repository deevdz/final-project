from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog
from .models import HomepageSlider


# Create your views here.
def index(request):
    """A view that displays the Homepage"""
    slides = HomepageSlider.objects.filter(status='published').order_by('?')[:3]
    blog_posts = Blog.objects.filter(status='published').order_by('-created_date')[:3]
    
    context = {
            'queryset': blog_posts,
            'slides': slides,
            }
    
    return render(request, 'index.html', context)
    
def about(request):
    """A view that displays the About Page"""
    return render(request, 'about.html',{})
    
