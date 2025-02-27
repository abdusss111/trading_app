import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from trading.routing import websocket_urlpatterns
from channels.auth import AuthMiddlewareStack

# Ensure Django settings are properly loaded before starting ASGI
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_proj.settings")
django.setup()

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),  # Handles HTTP requests
        "websocket": AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        ),
    }
)
