import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Order

class OrderBookConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("order_book", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("order_book", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        order = Order.objects.create(
            user_id=data["user_id"],
            product_id=data["product_id"],
            order_type=data["order_type"],
            quantity=data["quantity"],
            price=data["price"],
        )

        # Broadcast order to all connected clients
        await self.channel_layer.group_send(
            "order_book",
            {
                "type": "send_order",
                "order_id": order.id,
                "user_id": order.user.id,
                "product_id": order.product.id,
                "order_type": order.order_type,
                "quantity": order.quantity,
                "price": float(order.price),
            },
        )

    async def send_order(self, event):
        await self.send(text_data=json.dumps(event))
