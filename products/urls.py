from django.urls import path
from .views import CategoryList, CategoryCreate, CategoryRUD, CategoryRetrieve

urlpatterns = [
    path('category/list/', CategoryList.as_view()),
    path('category/add/', CategoryCreate.as_view()),
    path('category/<int:pk>/', CategoryRUD.as_view()),
    path('category/get/<int:pk>/', CategoryRetrieve.as_view())
]