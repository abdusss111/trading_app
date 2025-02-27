import django
from channels.routing import get_default_application

django.setup()
application = get_default_application()
from .celery import app as celery_app

__all__ = ("celery_app",)
