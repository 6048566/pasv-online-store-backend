from django.conf import settings
from django.core.management import call_command

from rest_framework import status
from rest_framework.test import APITestCase

from customers.models import Customer, User
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

    def test_create_user(self):
        # Создаем customer
        customer = self._create_customer()

        # Создаем запрос
        url = '/api/customer/registration/'
        data = dict(
            token=customer.token,
            username='Username',
            password='123456',
            email='email@gmail.com',
            first_name='first_name',
            last_name='last_name',
        )

        # валидируем ответ
        res = self.client.post(url, data, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(id=res.data['id'])
        # Если наш метод требует авторизацию по JWT
        # Можем передавать JWT используя эту конcтрукцию (JWT не нужно добавлять отдельно)
        self.client.force_authenticate(user=user)

        self.assertEqual(res.data['username'], user.username)
