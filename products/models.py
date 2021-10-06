from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    country = CountryField(null=False, blank=False)
    brewery = models.CharField(max_length=20)
    abv = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def rating(self):
        total = sum(int(review['rating']) for review in self.reviews.values())

        if self.reviews.count() > 0:
            return total / self.reviews.count()
        else:
            return 0


class Review(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, blank=False, related_name='reviews', on_delete=models.CASCADE)
    content = models.CharField(max_length=18, null=False, blank=False,)
    rating = models.IntegerField(null=False, blank=False,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    date_added = models.DateTimeField(auto_now_add=True)
