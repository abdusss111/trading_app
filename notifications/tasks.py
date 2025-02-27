from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_notification_email(user_email, subject, message):
    send_mail(
        subject,
        message,
        "no-reply@tradingapp.com",  # Change to your email sender
        [user_email],
        fail_silently=False,
    )
    return f"Email sent to {user_email}"
