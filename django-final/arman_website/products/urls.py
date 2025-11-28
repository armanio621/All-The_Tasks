from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_list, name='products'),  # /products/
    path('products/<int:pk>/', views.product_detail, name='product_detail'),  # /products/<id>/
]
