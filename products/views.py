from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
from .models import Product, Workshop
from taggit.models import Tag

# Create your views here.

def workshops(request):
    workshop_events = Product.objects.instance_of(Workshop).filter(status='published').order_by('-created_date')
    
    context = {
         'workshop_events': workshop_events
    }

    return render(request, 'workshops.html', context)
