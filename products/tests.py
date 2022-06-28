from django.conf import settings
from django.core.management import call_command

from rest_framework import status
from rest_framework.test import APITestCase


class ProductTest(APITestCase):
    """
    Получаем список продуктов без фильтров
    """
    def test_product_list_without_filters(self):
        # Первый делом нужно заполнить данные в базу созданную для тестов
        call_command('init_products')

        # Отправляем запрос
        url = '/api/product/all/'
        res = self.client.get(url)

        # Валидируем ответ
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # Так как мы знаем что в init_products лежит список из 4 значений
        self.assertEqual(len(res.data), 5)

    """
    Получаем список продуктов с фильтрами
    """
    def test_product_list_with_filters(self):
        # Первый делом нужно заполнить данные в базу созданную для тестов
        call_command('init_products')

        # Отправляем запрос
        url = '/api/product/all/'
        search_title = 'K2 PHASE PRO SKI-/SNOWBOARD HELMET BLACK'
        params = dict(
            title=search_title
        )
        res = self.client.get(url, params=params)

        # Валидируем ответ
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['result'][0]['title'], search_title)
