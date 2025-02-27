from celery import shared_task
from analytics.utils import update_trading_analytics

@shared_task
def run_daily_trading_analytics():
    update_trading_analytics()
    return "Trading Analytics Updated"
