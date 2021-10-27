from django.urls import path
from . import views

urlpatterns = [
    path('share_builds/', views.share_builds, name='share_builds'),
    path('create_post/', views.create_post, name='create_post'),
]
