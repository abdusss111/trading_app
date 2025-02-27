from django.db import models

class AnalyticsReport(models.Model):
    report_type = models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)
    report_file = models.FileField(upload_to='analytics/')

from trading.models import Order  # Assuming you have an Order model
from django.utils import timezone

class TradingAnalytics(models.Model):
    date = models.DateField(default=timezone.now, unique=True)
    total_trades = models.PositiveIntegerField(default=0)
    total_volume = models.PositiveIntegerField(default=0)  # Sum of quantities
    avg_trade_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Analytics for {self.date}"
