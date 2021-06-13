from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'time_created', 'time_checkout', 'time_delivery']

@admin.register(OrderProduct)
class OrderProductAmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity']
