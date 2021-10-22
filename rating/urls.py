from django.urls import path
from . import views

urlpatterns = [
    path('create_rating/', views.create_rating, name='create_rating'),
]