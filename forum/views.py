from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Forum
from .forms import CreatePostForm



def share_builds(request):
    """ A view to return share_builds page """
    # posts varible returns all of the posts in the Forum models
    # user variable returns the request.user converted to a string
    posts = Forum.objects.all()
    user = str(request.user)
    context = {
        "posts": posts,
        "user": user
        }
    return render(request, 'forum/share_builds.html', context)

@login_required()
def create_post(request):
    """ A view to add posts to the share builds page"""
    # form variable returns the CreatePostForm created in forms.py
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


@login_required()
def edit_post(request, post_id):
    """A view to Edit the post and return to the share builds page"""
    # post varible returns the id of the post you want to update
    # user variable returns the request.user converted to a string
    post = get_object_or_404(Forum, pk=post_id)
    user = str(request.user)

    if post.poster.username == user:
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
    else:
        messages.warning(request, 'Not allowed to update other users posts! ')
        return redirect('home')

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'forum/edit_post.html', context)


@login_required()
def delete_post(request, post_id):
    """A view to Delete the post and return to the share builds page"""
    # post varible returns the id of the post you want to update
    # user variable returns the request.user converted to a string
    post = get_object_or_404(Forum, pk=post_id)
    user = str(request.user)

    context = {
        'post': post,
    }
    if post.poster.username == user:
        if request.method == 'POST':
            post.delete()
            messages.success(request, 'Successfully deleted post!')
            return redirect(reverse('share_builds'))
    else:
        messages.warning(request, 'Not allowed to delete other users posts! ')
        return redirect('home')
    
    return render(request, 'forum/delete_post.html', context)
