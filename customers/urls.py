from django.urls import path
from .views import *

urlpatterns = [
    path('create/', customer_create)
]