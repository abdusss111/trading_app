from django.http import JsonResponse
from .tasks import send_notification_email

def send_test_email(request):
    user_email = "user@example.com"  # Replace with real user email
    send_notification_email.delay(user_email, "Trade Update", "Your trade has been executed.")
    return JsonResponse({"message": "Email sent asynchronously!"})
