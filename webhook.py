# webhook.py
import requests
import json
from datetime import datetime

def send(webhook_url: str, username: str, status: str, details: str = ""):
    """
    status = "SUCCESS" or "FAILED"
    """
    color = 0x00ff00 if status == "SUCCESS" else 0xff0000
    embed = {
        "title": f"Account {status}",
        "description": f"**{username}**",
        "color": color,
        "fields": [
            {"name": "Time", "value": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "inline": True},
            {"name": "Details", "value": details or "—", "inline": False}
        ],
        "footer": {"text": "BloxFruits Bot • Hosted on YOUR SERVER"}
    }
    payload = {"embeds": [embed]}
    try:
        requests.post(webhook_url, json=payload, timeout=5)
    except Exception as e:
        print(f"Webhook failed: {e}")
