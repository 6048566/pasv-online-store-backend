import django_filters
from .models import Product

class ProductFilter(django_filters.rest_framework.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    brand = django_filters.CharFilter(field_name='brand__title', lookup_expr='contains')
    brand_id = django_filters.NumberFilter(field_name='brand__id', lookup_expr='exact')
    title = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    class Meta:
        model = Product
        fields = ['brand', 'title', 'min_price', 'max_price']