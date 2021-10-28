from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.validators import ValidationError
from django.contrib import messages
from .models import Forum
from .forms import CreatePostForm


import datetime


def share_builds(request):
    """ A view to return share_builds page """
    posts = Forum.objects.all()
    context = {"posts": posts}
    return render(request, 'forum/share_builds.html', context)


def create_post(request):
    """ Adds posts to the share builds page"""
    form = CreatePostForm()
    context = {
        "form": form
    }
    if request.method == "POST":
        post_form = CreatePostForm(request.POST, request.FILES)
        if post_form.is_valid:
            post = post_form.save(commit=False)
            post.poster = request.user
            print(post)
            post.save()
            messages.success(request, 'Build Successfully Shared')
            return redirect('share_builds')
        else:
            messages.error(request, 'Failed to update post. Please esnure the form is valid.')


    return render(request, 'forum/create_post.html', context)


def edit_post(request, post_id):
    """Edit the post and return to the share builds page"""
    post = get_object_or_404(Forum, pk=post_id)
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('share_builds'))
        else:
            messages.error(request, 'Failed to update post. Please esnure the form is valid.')
    else:
        form = CreatePostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'forum/edit_post.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Forum, pk=post_id)

    context = {
        'post': post,
    }

    if request.method == 'POST':
        post.delete()
        messages.success(request,'Successfully deleted post!')
        return redirect(reverse('share_builds'))
    
    return render(request, 'forum/delete_post.html', context)
