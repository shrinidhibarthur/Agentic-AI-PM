
from jira import JIRA

def create_jira_ticket(issue, config):
    jira = JIRA(server=config["url"], basic_auth=(config["email"], config["api_token"]))
    issue_dict = {
        'project': {'key': config["project_key"]},
        'summary': f"KPI Alert: {issue['issue']}",
        'description': f"Automated alert based on threshold breach.\nDetails: {issue}",
        'issuetype': {'name': 'Task'},
    }
    jira.create_issue(fields=issue_dict)
