from django.contrib import admin
from .models import Address, Order

# Register your models here.
admin.site.register(Order)
admin.site.register(Address)
