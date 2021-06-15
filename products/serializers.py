from rest_framework import serializers
from .models import Category, Product, ProductReview, Brand
from django.conf import settings

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'is_active']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'



class BrandField(serializers.RelatedField):
    def to_representation(self, value):
        return {"id": value.id, "title": value.title}

class PhotoField(serializers.RelatedField):
    def to_representation(self, value):
        try:
            return settings.BASE_DOMAIN + value.url
        except:
            return settings.BASE_DOMAIN + '/media/images/no_photo.jpg'


class ProductRetrieveSerializer(serializers.ModelSerializer):
    reviews = ProductReviewSerializer(many=True, read_only=True)
    brand = BrandField(many=False, read_only=True)
    photo = PhotoField(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'old_price', 'quantity', 'photo', 'brand', 'description', 'reviews']


class ProductPreviewSerializer(serializers.ModelSerializer):
    brand = BrandField(many=False, read_only=True)
    photo = PhotoField(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'old_price', 'photo', 'brand']


class BrandRetrieveWithProductSerializer(serializers.ModelSerializer):
    products = ProductPreviewSerializer(many=True, read_only=True)
    class Meta:
        model = Brand
        fields = ['id', 'title', 'products']


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title']