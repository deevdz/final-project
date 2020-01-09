from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.utils import timezone
from blog.models import Blog
from products.models import Workshop
from .models import HomepageSlider
from .forms import ContactForm
    

# Create your views here.
def index(request):
    """A view that displays the Homepage"""
    slides = HomepageSlider.objects.filter(status='published').order_by('?')[:3]
    blog_posts = Blog.objects.filter(status='published').order_by('-created_date')[:3]
    upcoming_workshops = Workshop.objects.filter(status='published', workshop_end_date__gt=timezone.now()).order_by('?')[:1]
    
    context = {
            'queryset': blog_posts,
            'slides': slides,
            'upcoming_workshops': upcoming_workshops
            }
    
    return render(request, 'index.html', context)
    
def about(request):
    """A view that displays the About Page"""
    return render(request, 'about.html',{})

def what_do_i_need(request):
    """A view that displays the What Do I need Page"""
    return render(request, 'what-do-i-need.html',{})

def bikram_hot_yoga(request):
    """A view that displays the Hot Yoga Page"""
    return render(request, 'bikram-hot-yoga.html',{})  

def meditation(request):
    """A view that displays the Meditation Page"""
    return render(request, 'meditation.html',{})    
    
def pregnancy_yoga(request):
    """A view that displays the Pregnancy Yoga Page"""
    return render(request, 'pregnancy-yoga.html',{})   
    
def reformer_bed(request):
    """A view that displays the Reformer Bed Page"""
    return render(request, 'reformer-bed.html',{})    
    
def timetable(request):
    """A view that displays the Timetable Page"""
    return render(request, 'timetable.html',{})
    
def total_barre(request):
    """A view that displays the Total Barre Page"""
    return render(request, 'total-barre.html',{})    
    
def yogalates(request):
    """A view that displays the Yogalates Page"""
    return render(request, 'yogalates.html',{})    
    
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