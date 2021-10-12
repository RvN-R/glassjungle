from django.shortcuts import render
from .models import Product

# Create your views here.


def empty_terrariums(request):
    """A view to return empty_terrariums.html"""
    # products = Product.objects.all()
    products = Product.objects.filter(category='empty terrarium')
    context = {
        'products': products,
    }

    print(products)

    return render(request, 'products/empty_terrariums.html', context)
