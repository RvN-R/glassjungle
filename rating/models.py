from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Rating(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=False, blank=False)
    rating = models.IntegerField(null=False, blank=False, validators=[MaxValueValidator(5, message=None), MinValueValidator(0, message=None)])
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

