from django.contrib import admin
from .models import Product, Category, Rating

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
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
    list_display = (
        'friendly_name',
        'name',
    )

class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'rating',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rating, RatingAdmin)
