from django.urls import path
from .views import order_book

urlpatterns = [
    path("order_book/", order_book, name="order_book"),
]
