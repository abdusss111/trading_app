from django.contrib import admin
from .models import AnalyticsReport, TradingAnalytics

@admin.register(AnalyticsReport)
class AnalyticsReportAdmin(admin.ModelAdmin):
    list_display = ('report_type', 'generated_at', 'report_file')
    search_fields = ('report_type',)
    list_filter = ('generated_at',)

@admin.register(TradingAnalytics)
class TradingAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('date', 'total_trades', 'total_volume', 'avg_trade_value')
    search_fields = ('date',)
    list_filter = ('date',)
