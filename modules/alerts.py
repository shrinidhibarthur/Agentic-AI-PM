
import requests

def send_teams_alert(issue, webhook_url):
    payload = {
        "title": issue["title"],
        "text": issue["description"]
    }
    requests.post(webhook_url, json=payload)
