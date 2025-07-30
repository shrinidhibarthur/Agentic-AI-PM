
def check_kpis(config):
    # Simulated KPI check
    # In production, pull data from analytics or BI tool
    issues = []
    simulated_drop = 6  # percent drop in conversion rate
    if simulated_drop > config["thresholds"]["conversion_drop_percent"]:
        issues.append({
            "title": "Conversion Rate Drop",
            "description": f"Conversion rate dropped by {simulated_drop}%",
            "priority": "High"
        })
    return issues
