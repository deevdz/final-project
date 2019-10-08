from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def index(request):
    """A view that displays the Homepage"""
    return render(request, 'index.html',{})
    
def about(request):
    """A view that displays the About Page"""
    return render(request, 'about.html',{})
    
