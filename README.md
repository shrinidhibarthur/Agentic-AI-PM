Agentic AI PM — Real-Time & Automated Product Management Assistant
What It Is
Agentic AI PM is an AI-powered, event-driven assistant designed to support Product Managers by:
• Continuously monitoring product metrics in real-time
• Running daily AI-powered analysis of key KPIs
• Sending instant alerts to Microsoft Teams when thresholds are breached
• Auto-creating JIRA tickets for detected issues
• Using a configurable config.json for thresholds & polling intervals

How to Use
Setup
1. Clone / Download the repo.
2. Install dependencies:
bash
CopyEdit
pip install -r requirements.txt
3. Set environment variables:
bash
CopyEdit
export TEAMS_WEBHOOK_URL="https://your-teams-webhook"
export JIRA_URL="https://your-jira-instance.atlassian.net"
export JIRA_API_KEY="your-api-key"
export JIRA_USER="your-email"
4. Adjust thresholds in config.json without touching code.
Run
• Unified Service (Daily + Real-Time)
bash
CopyEdit
python run_unified_service.py
• The service will:
✅ Run daily summary at 9:00 AM
✅ Monitor metrics continuously
✅ Alert Teams instantly when issues are detected
✅ Create JIRA tasks automatically

Why It’s Required
• Faster Issue Detection: PMs often rely on retroactive reports. By the time anomalies are spotted, impact is already felt. This tool detects issues as they happen.
• Reduced Manual Overhead: No more refreshing dashboards or manually raising tickets. The AI handles monitoring, analysis, and action.
• Centralized Workflow: Direct integration with Microsoft Teams and JIRA means PMs never miss an important alert.

Impact
📈 Speed: Detects and alerts in minutes, not days.
📊 Accuracy: AI-powered analysis reduces false alarms & surfaces root causes faster.
⏳ Efficiency: Saves PMs 5–10 hours/week in manual monitoring.
💰 Business Value: Faster detection → quicker fixes → reduced revenue loss.
Example:
If conversion rate drops by 5%, and average daily revenue is $200K, early detection could save $10K+ per day until resolved.

