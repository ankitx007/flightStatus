from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_flight_update(flight_data):
    producer.send('flight_notifications', flight_data)
    producer.flush()
