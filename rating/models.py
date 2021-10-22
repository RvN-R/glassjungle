from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Rating(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=False, blank=False)
    rating = models.IntegerField(null=False, blank=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

