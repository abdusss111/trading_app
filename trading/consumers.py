import json
from channels.generic.websocket import AsyncWebsocketConsumer

class OrderBookConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("order_book", self.channel_name)
        await self.accept()
        print(f"WebSocket Connected: {self.channel_name}")  # Debugging

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("order_book", self.channel_name)
        print(f"WebSocket Disconnected: {self.channel_name}")  # Debugging

    async def receive(self, text_data):
        data = json.loads(text_data)
        print("Received from Client:", data)  # Debugging

        # Broadcast to all WebSocket clients
        await self.channel_layer.group_send(
            "order_book",
            {
                "type": "send_order",
                "order_id": data["order_id"],
                "order_type": data["order_type"],
                "quantity": data["quantity"],
                "price": data["price"],
            },
        )

    async def send_order(self, event):
        print("Sending to Clients:", event)  # Debugging
        await self.send(text_data=json.dumps(event))
