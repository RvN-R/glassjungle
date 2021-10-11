from django.shortcuts import render
from .models import Product

# Create your views here.


def empty_terrariums(request):
    """A view to return empty_terrariums.html"""
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products/empty_terrariums.html', context)
