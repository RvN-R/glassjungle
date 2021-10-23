from django.urls import path
from . import views

urlpatterns = [
    path('create_rating/<product_id>', views.create_rating, name='create_rating'),
    path('update_rating/<rating_id>', views.update_rating, name='update_rating'),
]