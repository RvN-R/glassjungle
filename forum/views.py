from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.validators import ValidationError
from django.contrib import messages
from .models import Forum


import datetime


def share_builds(request):
    """ A view to return share_builds page """
    context = {}
    return render(request, 'forum/share_builds.html')