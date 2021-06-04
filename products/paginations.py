from rest_framework import pagination
from rest_framework.response import Response
from math import ceil

class ProductPagination(pagination.PageNumberPagination):
    page_size = 2
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'page': int(self.request.query_params.get(self.page_query_param, 1)),
            'pages': ceil(self.page.paginator.count / self.page_size),
            'count': self.page.paginator.count,
            'result': data
        })