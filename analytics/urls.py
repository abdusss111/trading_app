from django.urls import path
from .celery_report import generate_report

urlpatterns = [
    path('analytics/report/', generate_report, name="generate_report"),
]
