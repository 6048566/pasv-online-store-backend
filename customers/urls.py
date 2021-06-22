from django.urls import path
from .views import *

urlpatterns = [
    path('create/', customer_create),
    path('registration/', UserCreate.as_view()),
    path('myorders/', MyOrders.as_view()),
    path('getuser/', GetAuthCustomer.as_view()),
]