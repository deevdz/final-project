from django.contrib import admin
from .models import Address, Order


# Admin - Order: What to display in the backend view
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'ordered')

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Address)