from django.shortcuts import render, HttpResponse
from rest_framework import generics
import uuid
import json
from .models import Customer


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