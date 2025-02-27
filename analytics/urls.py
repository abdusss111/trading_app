from django.urls import path
from .celery_report import generate_report
from .views import get_trading_analytics

urlpatterns = [
    path('report/', generate_report, name="generate_report"),
    path('trading-analytics/', get_trading_analytics, name="trading_analytics"),
]