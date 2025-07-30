
from modules.monitor import check_kpis
from modules.notifier import send_teams_alert
from modules.jira_creator import create_jira_ticket
import json

def main():
    with open("config/config.json") as f:
        config = json.load(f)

    issues = check_kpis(thresholds=config["thresholds"])
    for issue in issues:
        send_teams_alert(issue, config["teams_webhook_url"])
        create_jira_ticket(issue, config["jira"])

if __name__ == "__main__":
    main()
