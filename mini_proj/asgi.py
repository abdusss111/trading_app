import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from trading.routing import websocket_urlpatterns

# Set Django settings before setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_proj.settings")
django.setup()

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)  # Routes WebSockets to consumers
        ),
    }
)
