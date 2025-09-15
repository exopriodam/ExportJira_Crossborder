from datetime import datetime
from jira_client import JiraClient
from transformer import IssueTransformer
from exporter import CsvExporter
from config import JQL,DATE_TO_USE_START,DATE_TO_USE_END

def run():
    jira_client = JiraClient()
    date_start= " AND Created >= "+ datetime.strptime(DATE_TO_USE_START, "%d/%m/%Y").strftime("%Y-%m-%d") if DATE_TO_USE_START else ""
    date_end = " AND Created <= "+ datetime.strptime(DATE_TO_USE_END, "%d/%m/%Y").strftime("%Y-%m-%d")  if DATE_TO_USE_END else ""
    jql = JQL + date_start + date_end

    issues = jira_client.fetch_issues(jql)
    data = [IssueTransformer.transform(issue) for issue in issues]

    exporter = CsvExporter("jira_issues.csv")
    filename = exporter.export(data)

    print(f"✅ Export terminé : {filename}")

if __name__ == "__main__":
    run()
