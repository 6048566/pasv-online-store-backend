from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework import generics
import uuid
import json
from .models import Customer
from .serializers import *

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

# class CustomerCreate(generics.CreateAPIView):
#     def create(self, request, *args, **kwargs):

def customer_create(request):
    if request.method == 'POST':
        try:
            customer_token = str(uuid.uuid4())
            Customer.objects.create(token=customer_token)
            response = {
                "status": True,
                "customer_token": customer_token
            }
        except BaseException:
            response = {
                "status": False,
            }
    else:
        response = {
            "status": False
        }
    return HttpResponse(json.dumps(response))

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User



class MyOrders(generics.ListAPIView):
    serializer_class = MyOrdersSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    def get_queryset(self):
        return Order.objects.filter(customer__user=self.request.user)


# def get_auth_customer(request):
#     if request.user.is_authenticated == True:
#         try:
#             customer = Customer.objects.get(user=request.user)
#             return HttpResponse(json.dumps(customer))
#         except BaseException:
#             return HttpResponse()


class GetAuthCustomer(generics.RetrieveAPIView):
    serializer_class = CustomerSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        customer = get_object_or_404(Customer, user=self.request.user)
        return customer
