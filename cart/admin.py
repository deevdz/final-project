from django.contrib import admin
from .models import OrderLineItem


# Admin - OrderLineItem: What to display in the backend view
class OrderLineItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'created', 'purchased')

# Register your models here.
admin.site.register(OrderLineItem, OrderLineItemAdmin)
