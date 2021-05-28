from django.urls import path
from .views import CategoryList

urlpatterns = [
    path('category/list/', CategoryList.as_view())
]