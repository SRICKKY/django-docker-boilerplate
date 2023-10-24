from django.urls import path

from .views import (
    OrderCreateView,
    OrderListView,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/', OrderListView.as_view(), name='order-list'),
]
