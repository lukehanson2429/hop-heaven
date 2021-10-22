""" Imports  """
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from products.models import Product


class Rating(models.Model):
    """ Custom Ratings Model  """
    product = models.ForeignKey(
        Product, null=False, blank=False,
        related_name='ratings', on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, null=False, blank=False,
        related_name='ratings', on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        null=False, blank=False,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
