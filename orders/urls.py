from django.urls import path
from .views import *

urlpatterns = [
    path('cart/add/', PutToCart.as_view())
]