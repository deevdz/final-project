from django.db import models
from django.conf import settings
from django.utils import timezone
from tinymce import HTMLField
from django.urls import reverse
from taggit.managers import TaggableManager
from polymorphic.models import PolymorphicModel

# Create your models here.

class Product(PolymorphicModel):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published','Published'),
        )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    description = HTMLField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')
    tags = TaggableManager()
    image = models.ImageField(upload_to="img")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('products', args=[self.slug])
        
class Workshop(Product):
    
    WORKSHOP_LOCATIONS = (
        ('headford', 'Headford Wellbeing Centre'),
        ('burren','Burren'),
        )
    workshop_start_date = models.DateField(blank=True, default=timezone.now)
    workshop_end_date = models.DateField(blank=True, default=timezone.now)
    workshop_start_time = models.TimeField(blank=True)
    workshop_end_time = models.TimeField(blank=True)
    available_places = models.IntegerField(default=10)
    workshop_location = models.CharField(max_length=940, choices=WORKSHOP_LOCATIONS, default='headford')
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('workshops', args=[self.slug])
