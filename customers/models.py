from django.db import models

# Create your models here.

class Customer(models.Model):
    class Meta:
        db_table = 'customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    first_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='First name')
    last_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Last name')
    phone = models.BigIntegerField(null=True, blank=True, verbose_name='Phone')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='Email')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Time created')
    token = models.CharField(max_length=200, null=False, blank=False, editable=False, verbose_name='Token')


class CustomerAddress(models.Model):
    class Meta:
        db_table = 'customers_addresses'
        verbose_name = 'Customer address'
        verbose_name_plural = 'Customers addresses'

    customer = models.ForeignKey(Customer, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Customer')
    country = models.CharField(null=False, blank=False, max_length=200, verbose_name='Country')
    city = models.CharField(null=False, blank=False, max_length=200, verbose_name='City')
    post_code = models.IntegerField(null=False, blank=False, verbose_name='Post code')
    address = models.CharField(null=False, blank=False, max_length=200, verbose_name='Address')

