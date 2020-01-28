from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
from .models import Product, Workshop
from taggit.models import Tag


# Display products on the shop page based on product type
def products(request):
    all_vouchers = Product.objects.filter(product_type='voucher',
                                          status='published'
                                          ).order_by('-created_date')
    all_classes = Product.objects.filter(product_type='class',
                                         status='published'
                                         ).order_by('-created_date')
    context = {
         'all_vouchers': all_vouchers,
         'all_classes': all_classes
    }

    return render(request, 'shop.html', context)


# Display workshop products only on the workshop page
# Only display workshops that are still in date
def workshops(request):
    workshops = Product.objects.instance_of(Workshop).filter(status='published'
                                                             ).order_by('-created_date')
    workshop_events = workshops.filter(Q(Workshop___workshop_end_date__gt=timezone.now()))

    context = {
         'workshop_events': workshop_events
    }

    return render(request, 'workshops.html', context)


# Display the workshop details on there own page
def workshop_detail(request, slug):
    workshop_details = get_object_or_404(Product, slug=slug)

    context = {
         'workshop_details': workshop_details
    }

    return render(request, 'workshop_detail.html', context)
