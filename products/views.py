from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
from .models import Product, Workshop
from taggit.models import Tag

# Create your views here

def products(request):
    all_vouchers = Product.objects.filter(product_type='voucher', status='published').order_by('-created_date')
    all_classes = Product.objects.filter(product_type='class', status='published').order_by('-created_date')
    context = {
         'all_vouchers': all_vouchers,
         'all_classes': all_classes
    }

    return render(request, 'shop.html', context)


def workshops(request):
    workshop_events = Product.objects.instance_of(Workshop).filter(status='published').order_by('-created_date')
    
    context = {
         'workshop_events': workshop_events
    }

    return render(request, 'workshops.html', context)
    
def workshop_detail(request, slug):
    workshop_details = get_object_or_404(Product, slug=slug)
    
    context = {
         'workshop_details': workshop_details
    }

    return render(request, 'workshop_detail.html', context)
    
