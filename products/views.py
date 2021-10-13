from django.shortcuts import render, get_object_or_404
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


def product_detail(request, id):
    """A view show indivdual product"""
    # products = Product.objects.get(id=pk)
    products = get_object_or_404(Product, pk=id)
    
    context = {
        'products': products
    }
    print(products)

    return render(request, 'products/product_detail.html', context)
