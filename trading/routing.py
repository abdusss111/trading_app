from django.urls import re_path
from .consumers import OrderBookConsumer

websocket_urlpatterns = [
    re_path(r"ws/trading/$", OrderBookConsumer.as_asgi()),
]
