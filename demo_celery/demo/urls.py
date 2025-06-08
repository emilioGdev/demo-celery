from django.urls import path
from .views import create_demo

urlpatterns = [
    path('demo/', create_demo, name='create_demo'),
]
