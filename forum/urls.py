from django.urls import path
from . import views

urlpatterns = [
    path('share_builds/', views.share_builds, name='share_builds'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
