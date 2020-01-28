from django.contrib import admin
from .models import Product, Workshop


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',)
    prepopulated_fields = {'slug': ('title',)}


class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',)
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Product, ProductAdmin)
