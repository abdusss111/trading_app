import os
from celery import Celery

# Set the default Django settings module for Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_proj.settings")

app = Celery("mini_proj")

# Load settings from Django settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# Autodiscover tasks in all installed Django apps
app.autodiscover_tasks()