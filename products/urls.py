from django.urls import path
from . import views
urlpatterns = [
    path('empty_terrariums/', views.empty_terrariums, name='empty_terrariums'),
    path('full_terrariums/', views.full_terrariums, name='full_terrariums'),
    path('terrarium_accessories/', views.terrarium_accessories, name='terrarium_accessories'),
    path('<product_id>/', views.product_detail, name='product_detail'),
]