from analytics.models import TradingAnalytics
from trading.models import Order
from django.utils import timezone


def update_trading_analytics():
    today = timezone.now().date()

    # Get all trades for today
    trades_today = Order.objects.filter(created_at__date=today)

    if trades_today.exists():
        total_trades = trades_today.count()
        total_volume = sum(order.quantity for order in trades_today)
        avg_trade_value = sum(order.price * order.quantity for order in trades_today) / total_trades

        analytics, created = TradingAnalytics.objects.get_or_create(date=today)
        analytics.total_trades = total_trades
        analytics.total_volume = total_volume
        analytics.avg_trade_value = avg_trade_value
        analytics.save()

        print(f"✅ Updated Analytics for {today}")
