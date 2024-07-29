from twilio.rest import Client

def send_sms(phone_number, message):
    client = Client('ACfe8448a18711bf3bebae856030aa968b', 'c1ab30136eba7e106f45da960bfc336d')
    client.messages.create(
        to=phone_number,
        from_='+12085682066',
        body=message
    )
