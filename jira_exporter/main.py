from datetime import datetime
from jira_client import JiraClient
from transformer import IssueTransformer
from exporter import CsvExporter
import config_loader as config

def run():
    jira_client = JiraClient()
    date_start= " AND Created >= "+ datetime.strptime(config.DATE_TO_USE_START, "%d/%m/%Y").strftime("%Y-%m-%d") if config.DATE_TO_USE_START else ""
    date_end = " AND Created <= "+ datetime.strptime(config.DATE_TO_USE_END, "%d/%m/%Y").strftime("%Y-%m-%d")  if config.DATE_TO_USE_END else ""
    jql = config.JIRA_JQL + date_start + date_end

    issues = jira_client.fetch_issues(jql)
    data = [IssueTransformer.transform(issue) for issue in issues]

    exporter = CsvExporter("jira_issues.csv")
    filename = exporter.export(data)

    print(f"✅ Export terminé : {filename}")

if __name__ == "__main__":
    run()
