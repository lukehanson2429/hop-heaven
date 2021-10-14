""" Imports  """
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """ Display product model data for admin & order by category  """
    list_display = (
        'name',
        'category',
        'country',
        'brewery',
        'abv',
        'price',
        'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    """ Display category model data for admin  """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
