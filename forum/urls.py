from django.urls import path
from . import views

urlpatterns = [
    path('share_builds/', views.share_builds, name='share_builds'),
]
