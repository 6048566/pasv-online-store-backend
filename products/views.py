from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer
from .models import Category

# Create your views here.


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()