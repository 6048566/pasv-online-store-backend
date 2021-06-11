from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
# Create your views here.


class PutToCart(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response(status=status.HTTP_204_NO_CONTENT)