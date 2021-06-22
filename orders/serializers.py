from rest_framework import serializers
from customers.models import Customer
from .models import *
from datetime import datetime

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     instance.is_ordered = True
    #     instance.time_checkout = datetime.now()
    #     instance.save()
    #     return instance



class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'


