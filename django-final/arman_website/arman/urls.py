from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
]
