from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog


# Create your views here.
def index(request):
    """A view that displays the Homepage"""
    blog_posts = Blog.objects.filter(status='published').order_by('-created_date')[:3]
    
    context = {
            'queryset': blog_posts,
            }
    
    return render(request, 'index.html', context)
    
def about(request):
    """A view that displays the About Page"""
    return render(request, 'about.html',{})
    
