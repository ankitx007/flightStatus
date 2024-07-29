
import django
django.setup()

from kafka import KafkaConsumer
import json
from sms import send_sms
from email_notifications import send_email
from subscriptions.models import Subscriber

consumer = KafkaConsumer(
    'flight_notifications',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    print("Test", message)

    data = message.value
    flight_number = data['flight_number']
    status = data['status']

    subscribers = Subscriber.objects.filter(flight_number=flight_number, opt_in=True)


    for subscriber in subscribers:
        print(subscriber)
        # if subscriber.email:
        #     send_email(
        #         subscriber.email,
        #         f"Flight {flight_number} Status Update",
        #         f"The status of your flight {flight_number} is now {status}."
        #     )
        if subscriber.phone_number:
            send_sms(
                subscriber.phone_number,
                f"Your flight {flight_number} is now {status}."
            )
