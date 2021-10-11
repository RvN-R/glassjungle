from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('empty_terrariums/', views.empty_terrariums, name='empty_terrariums'),
]