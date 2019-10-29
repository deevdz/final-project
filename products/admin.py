from django.contrib import admin
from .models import Product, Workshop


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class WorkshopAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Product, ProductAdmin)