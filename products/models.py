""" Imports  """
from django.db import models
from django_countries.fields import CountryField

from django.core.validators import RegexValidator


class Category(models.Model):
    """ Categories Model  """
    class Meta:
        """ Admin Name  """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Custom Product Model  """
    category = models.ForeignKey(
        'Category', null=True, blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    country = CountryField(null=False, blank=False)
    brewery = models.CharField(max_length=20)
    abv = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(
        max_length=3, validators=[RegexValidator(r'^\d{1,10}$')]
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def rating(self):
        """ Return overall average rating for each product  """
        total = sum(int(rating['rating']) for rating in self.ratings.values())
        # If at least one rating return rating average otherwise 0
        if self.ratings.count() > 0:
            return total / self.ratings.count()
        else:
            return 0
