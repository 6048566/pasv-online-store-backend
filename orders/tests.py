from django.conf import settings
from django.core.management import call_command

from rest_framework import status
from rest_framework.test import APITestCase

from customers.models import Customer
from products.models import Product

import uuid
import json


class OrdersTest(APITestCase):
    def _create_customer(self):
        customer = Customer.objects.create(token=str(uuid.uuid4()))

        # Если наш метод требует авторизацию по JWT и модель customer является пользовательской моделью
        # Можем передавать JWT используя эту конcтрукцию (JWT не нужно добавлять отдельно)
        # self.client.force_authenticate(user=customer)

        return customer

    def _create_products(self):
        call_command('init_products')

    def test_update_card(self):
        # Создаем пользователя
        customer = self._create_customer()
        # Создаем список продуктов
        self._create_products()

        # Берем случайный продукт
        product = Product.objects.all().first()

        # Составляем запрос
        url = '/api/order/cart/update/'
        data = dict(
            token=customer.token,
            product_id=product.id,
            quantity=3
        )

        # Обработка ответа
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        data = json.loads(res.content)
        self.assertEqual(data['cart_items_count'], 1)
