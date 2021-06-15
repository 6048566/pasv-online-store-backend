from django.urls import path
from .views import *

urlpatterns = [
    path('cart/update/', update_cart),
    path('cart/list/<slug:customer_token>/', CartList.as_view())
]