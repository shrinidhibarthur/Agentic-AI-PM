
import requests

def send_teams_alert(issue, webhook_url):
    message = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "summary": "KPI Alert",
        "themeColor": "EA4300",
        "title": "🚨 Product KPI Alert",
        "text": f"Issue Detected: {issue['issue']}"
    }
    requests.post(webhook_url, json=message)
