from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from rating.models import Rating

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


def terrarium_accessories(request):
    """A view to return all terrarium_accessories.html"""
    products = Product.objects.exclude(name__icontains='terrarium')
    context = {
        'products': products
    }

    return render(request, 'products/terrarium_accessories.html', context)


def product_detail(request, product_id):
    """A view show indivdual product"""
    # products variable returns the product that matches the product_id
    # ratings variable returns any ratings assocaited with the product with
    # the product_id
    # user variable returns the request.user value.

    products = get_object_or_404(Product, pk=product_id)
    ratings = Rating.objects.filter(product_id=products)
    user = str(request.user)
    context = {
        'products': products,
        'ratings': ratings,
        'user': user
    }

    return render(request, 'products/product_detail.html', context)
