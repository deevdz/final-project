from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your Homepage Slider here.
class HomepageSlider(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published','Published'),
        )
    
    HEADLINE_ALIGNMENT_CHOICES = (
        ('slider-left-aligned', 'Left Aligned'),
        ('slider-right-aligned','Right Aligned'),        
        )
    
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to="img")
    urlpath =  models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    button = models.CharField(max_length=100)
    headline_alignment = models.CharField(max_length=50, choices=HEADLINE_ALIGNMENT_CHOICES, default='slider-left-aligned')

    def __str__(self):
        return self.title

