from django import forms
from django.forms import ModelForm
from .models import Forum


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Forum
        exclude = ('poster',)
