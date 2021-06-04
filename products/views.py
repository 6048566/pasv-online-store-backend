from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import *
from .models import Category, ProductCategory
from .paginations import ProductPagination


class CategoryList(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()
    def get_queryset(self):
        return Category.objects.filter(is_active=True)


class CategoryRetrieve(generics.RetrieveAPIView):
    serializer_class = CategoryRetrieveSerializer
    queryset = Category.objects.all()


class ProductRetrieve(generics.RetrieveAPIView):
    serializer_class = ProductRetrieveSerializer
    queryset = Product.objects.all()


class ProductListFromCategory(generics.ListAPIView):
    serializer_class = ProductPreviewSerializer

    def get_queryset(self):
        product_ids = ProductCategory.objects.filter(category_id=self.kwargs['category_id']).values('product_id')
        return Product.objects.filter(pk__in=product_ids)
        # SELECT * FROM products WHERE id in (1,2,3,4,5)


class ProductList(generics.ListAPIView):
    serializer_class = ProductPreviewSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination









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



