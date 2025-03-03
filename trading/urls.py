from django.urls import path
from .views import order_book, OrderDetailView, OrderListCreateView

urlpatterns = [
    path("order_book/", order_book, name="order_book"),

    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

]
