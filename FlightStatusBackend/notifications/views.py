from django.shortcuts import render

from subscriptions.models import Subscriber
from .producer import send_flight_update
from .firebase_notification import send_push_notification

def update_flight_status(request):
    flight_data = {
        'flight_number': 'XY123',
        'status': 'Delayed',
        'email': '7ankit4@gmail.com',
        'phone_number': '+918868090959'
    }
    send_flight_update(flight_data)
    return render(request, 'status_updated.html')


def notify_subscribers(flight_number, new_status):
    subscribers = Subscriber.objects.filter(flight_number=flight_number, opt_in=True)
    for subscriber in subscribers:
        # Assume `subscriber.fcm_token` contains the FCM token
        if subscriber.fcm_token:
            send_push_notification(subscriber.fcm_token, "Flight Status Update", f"Your flight {flight_number} is now {new_status}.")