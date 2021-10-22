from django import forms
from django.forms import ModelForm
from .models import Rating

class CreateRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ('poster', 'product_id')

