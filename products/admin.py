from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'manufacture',
        'description',
        'price',
        'size',
        'image',
    )


admin.site.register(Product, ProductAdmin)
