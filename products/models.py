from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    manufacture = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
