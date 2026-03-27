import os
import requests

def send_webhook(event: str, data: dict):
    webhook_url = os.getenv("WEBHOOK_URL")
    if not webhook_url:
        return False
    payload = {
        "event": event,
        "data": data
    }
    try:
        response = requests.post(webhook_url, json=payload, timeout=5)
        response.raise_for_status()
        return True
    except Exception as e:
        # Optionally log the error
        return False
