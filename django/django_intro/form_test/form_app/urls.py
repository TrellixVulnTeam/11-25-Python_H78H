from django.urls import path
from . import views

urlpartterns = [
    path('', views.index),
    path('create_user', views.create_user),
    path('success', views.success)
]