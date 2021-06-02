from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import CategorySerializer, CategoryListSerializer, CategoryRetrieveSerializer
from .models import Category


class CategoryList(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()
    def get_queryset(self):
        return Category.objects.filter(is_active=True)


class CategoryRetrieve(generics.RetrieveAPIView):
    serializer_class = CategoryRetrieveSerializer
    queryset = Category.objects.all()


##################################################################################################
# Код ниже опасен в рамках интернет магазина, т.к. любой может редактировать категории!
# Только для примера. Удалить перед деплоем.
##################################################################################################
# Начало
class CategoryCreate(generics.CreateAPIView):
    serializer_class = CategorySerializer


class CategoryRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def delete(self, request, *args, **kwargs):
        return Response({"message": "record deleted"}, status=status.HTTP_200_OK)

# Конец
##################################################################################################



