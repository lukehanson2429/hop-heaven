from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator


class Rating(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, blank=False, related_name='ratings', on_delete=models.CASCADE)
    rating = models.IntegerField(null=False, blank=False,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    date_added = models.DateTimeField(auto_now_add=True)
