from django.contrib import admin
from .models import HomepageSlider


# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')

# Register your models here.
admin.site.register(HomepageSlider, SliderAdmin)
