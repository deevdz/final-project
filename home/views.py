from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from blog.models import Blog
from .models import HomepageSlider
from .forms import ContactForm
    

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
    
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_form_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            subject = 'Contact Form from Website'
            message = content
            from_email = settings.EMAIL_HOST_USER
            to_list = [request.user.email, settings.EMAIL_HOST_USER]
            send_mail (subject, message, from_email, to_list, fail_silently=True)
            messages.success(request, "Success. Thanks for getting in touch!")
    return render(request, 'contact.html', {'form': form_class,})