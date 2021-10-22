from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Rating


def create_rating(request):
    """A view to return create_rating.html"""
    context = {
    }
    
    return render(request, 'rating/create_rating.html', context)

