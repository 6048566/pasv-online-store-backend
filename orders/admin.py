from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Customer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['token', 'last_name', 'first_name', 'phone', 'email', 'time_created']
    search_fields = ['last_name', 'first_name']
