""" Imports """
from django.contrib import admin
from .models import Rating

# Register your models here.

class RatingAdmin(admin.ModelAdmin):
    """ Display model data in Admin """
    list_display = (
        'product',
        'user',
        'rating',
    )


admin.site.register(Rating, RatingAdmin)
