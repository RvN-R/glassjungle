from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Rating
from .forms import CreateRatingForm


def create_rating(request):
    """A view to return create_rating.html"""
    form = CreateRatingForm()
    context = {
        'form': form
    }
    
    return render(request, 'rating/create_rating.html', context)

