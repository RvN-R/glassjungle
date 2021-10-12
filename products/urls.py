from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('empty_terrariums/', views.empty_terrariums, name='empty_terrariums'),
    path('full_terrariums/', views.full_terrariums, name='full_terrariums'),
    path('product_detail/', views.product_detail, name='product_detail'),
]