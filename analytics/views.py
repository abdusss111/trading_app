from django.http import JsonResponse
from analytics.models import TradingAnalytics
from django.utils import timezone

def get_trading_analytics(request):
    today = timezone.now().date()
    analytics = TradingAnalytics.objects.filter(date__lte=today).order_by("-date")[:7]  # Last 7 days

    data = [
        {
            "date": entry.date,
            "total_trades": entry.total_trades,
            "total_volume": entry.total_volume,
            "avg_trade_value": entry.avg_trade_value,
        }
        for entry in analytics
    ]

    return JsonResponse({"analytics": data})
