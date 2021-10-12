from django.shortcuts import render
from .models import Product

# Create your views here.


def empty_terrariums(request):
    """A view to return empty_terrariums.html"""
    products = Product.objects.filter(category='empty terrarium')
    context = {
        'products': products,
    }
    
    return render(request, 'products/empty_terrariums.html', context)


def full_terrariums(request):
    """A view to return full_terrariums.html"""
    products = Product.objects.filter(category='full terrarium')
    context = {
        'products': products,
    }
    
    return render(request, 'products/full_terrariums.html', context)
