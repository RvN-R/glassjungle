from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Rating
from .forms import CreateRatingForm
from products.models import Product

import datetime


def create_rating(request, product_id):
    """A view to return create_rating.html"""
    product = get_object_or_404(Product, pk=product_id)
    user = request.user
    form = CreateRatingForm()
    context = {
        'form': form,
        'product': product
        }
    if request.method == 'POST':
        form_data = {
            "comment": request.POST['comment'],
            "rating": request.POST['rating'],
        }
        rating_form = CreateRatingForm(form_data)
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.poster = request.user
            rating.product_id = product
            rating.updated = datetime.datetime.now()
            rating.created = datetime.datetime.now()
            rating.save()
            messages.success(request, 'Rating Successfully added!')
            return redirect(reverse('product_detail', args=[product.id]))
    
    return render(request, 'rating/create_rating.html', context)


def update_rating(request, rating_id):
    """A view to return update_rating.html"""
    rating = get_object_or_404(Rating, pk=rating_id)
    form = CreateRatingForm(instance=rating)
    context = {
        'rating': rating,
        'form': form
    }
    if request.method == 'POST':
        form = CreateRatingForm(request.POST, instance=rating)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rating Successfully Updated!')
            return redirect(reverse('product_detail', args=[rating.id]))
    return render(request, 'rating/update_rating.html', context)
