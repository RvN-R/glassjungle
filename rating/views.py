from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.validators import ValidationError
from django.contrib import messages
from .models import Rating
from .forms import CreateRatingForm
from products.models import Product

import datetime

@login_required
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
        else:
            messages.error(request, "Please rate product between 0 and 5")
        

        # if ValidationError:
        #     messages.error(request, "Please rate product between 0 and 5")
            # form_data = {
            #     "comment": request.POST['comment'],
            #     "rating": request.POST['rating'],
            # }
            # rating_form = CreateRatingForm(form_data)
            # if rating_form.is_valid():
            #     rating = rating_form.save(commit=False)
            #     rating.poster = request.user
            #     rating.product_id = product
            #     rating.updated = datetime.datetime.now()
            #     rating.created = datetime.datetime.now()
            #     rating.save()
            #     messages.success(request, 'Rating Successfully added!')
            #     return redirect(reverse('product_detail', args=[product.id]))
        
          
   
    return render(request, 'rating/create_rating.html', context)


@login_required
def update_rating(request, rating_id):
    """A view to return update_rating.html"""
    # rating varible returns the id of the rating you want to update
    # product varible returns the product attached to that rating
    # user variable returns the request.user converted to a string
    rating = get_object_or_404(Rating, pk=rating_id)
    product = Product.objects.get(name=rating.product_id)
    user = str(request.user)
    form = CreateRatingForm(instance=rating)
    context = {
        'rating': rating,
        'form': form
    }
    if rating.poster.username == user:
        if request.method == 'POST':
            form = CreateRatingForm(request.POST, instance=rating)
            if form.is_valid():
                form.save()
                messages.success(request, 'Rating Successfully Updated!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, "Please rate product between 0 and 5")


            # if ValidationError:
            #     print('recieved validation error')
            #     print(ValidationError)
            #     messages.error(request, "Please rate product between 0 and 5")
            #     form = CreateRatingForm(request.POST, instance=rating)
            #     if form.is_valid():
            #         form.save()
            #         messages.success(request, 'Rating Successfully Updated!')
            #         return redirect(reverse('product_detail', args=[product.id]))

        # try:
        #     form = CreateRatingForm(request.POST, instance=rating)
        #     if form.is_valid():
        #         form.save()
        #         messages.success(request, 'Rating Successfully Updated!')
        #         return redirect(reverse('product_detail', args=[product.id]))
        # except ValidationError as e:
        #     print('recieved validation error')
        #     print(ValidationError)
        #     messages.error(request, "Please rate product between 0 and 5")
            
    else:
        messages.warning(request, 'Not allowed to update other users ratings!')
        return redirect('home') 

    return render(request, 'rating/update_rating.html', context)


@login_required
def delete_rating(request, rating_id):
    """A view to return delete_rating"""
    # rating varible returns the id of the rating you want to delete
    # product varible returns the product attached to that rating.
    # user variable returns the request.user converted to a string  
    rating = get_object_or_404(Rating, pk=rating_id)
    product = Product.objects.get(name=rating.product_id)
    user = str(request.user)
    context = {
        'rating': rating,
    }
    if rating.poster.username == user:
        if request.method == 'POST':
            rating.delete()
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        messages.warning(request, 'Not allowed to delete other users ratings!')
        return redirect('home')
  
    return render(request, 'rating/delete_rating.html', context)
