from celery import shared_task
from datetime import datetime

@shared_task
def generate_report():
    report = AnalyticsReport(report_type="Trading Summary", generated_at=datetime.now())
    report.save()
    return "Report Generated"
