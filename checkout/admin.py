from django.contrib import admin
from .models import Address, Order


# Admin - Order: What to display in the backend view
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'ordered')
    
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'address_line_1',
                    'address_line_2', 'town', 'county',
                    'postcode')

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)