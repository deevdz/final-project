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


# Generate the views for the homepage
# Display Slides, Blog Posts and Upcoming Workshops
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


# View to display About Page
def about(request):
    return render(request, 'about.html', {})


# View to display What Do I Need Page
def what_do_i_need(request):
    return render(request, 'what-do-i-need.html', {})


# View to display Hot Yoga Page
def bikram_hot_yoga(request):
    return render(request, 'bikram-hot-yoga.html', {})


# View to display Meditation Page
def meditation(request):
    return render(request, 'meditation.html', {})


# View to display Pregnancy Yoga Page
def pregnancy_yoga(request):
    return render(request, 'pregnancy-yoga.html', {})


# View to display Reformer Bed Page
def reformer_bed(request):
    return render(request, 'reformer-bed.html', {})


# View to display Timetable Page
def timetable(request):
    return render(request, 'timetable.html', {})


# View to display Total Barre Page
def total_barre(request):
    return render(request, 'total-barre.html', {})


# View to display Yogalates Page
def yogalates(request):
    return render(request, 'yogalates.html', {})


# View to display Contact Page
def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the contact form with the
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
            to_list = [contact_email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email,
                      to_list, fail_silently=True)
            messages.success(request, "Thank you for contacting us! Someone will be in touch soon.")
    return render(request, 'contact.html', {'form': form_class, })


# View to display 404 Page
def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "404.html", status=404)


# View to display 500 Page
def handler500(request):
    """ Error Handler 500 - Internal Server Error """
    return render(request, "500.html", status=500)
