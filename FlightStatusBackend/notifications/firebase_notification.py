import requests

def send_push_notification(fcm_token, title, body):
    server_key = 'YOUR_SERVER_KEY'
    headers = {
        'Authorization': f'key={server_key}',
        'Content-Type': 'application/json',
    }
    data = {
        'to': fcm_token,
        'notification': {
            'title': title,
            'body': body,
        }
    }
    response = requests.post('https://fcm.googleapis.com/fcm/send', headers=headers, json=data)
    print(response.status_code, response.json())
