from __future__ import annotations
import pandas as pd
from jira import JIRA

#file = "config.json"
#config = json.load(open(file))
#jira = JIRA(server="https://it-projects.just.fgov.be/",
#                      basic_auth=("svcshrcrossdev01@just.fgov.be", "fa$tLemur37"),
#                     validate=True,
#                    proxies={"http": "http://10.235.1.14:8080", "https": "http://10.235.1.14:8080"})
jira = JIRA(server="https://it-projects.just.fgov.be/",
                       basic_auth=("svcshrcrossdev01@just.fgov.be", "fa$tLemur37"),
                       validate=True)
jql_query = "project = BOT AND status = Pending AND cf[10834] = \"Ready for digital upload\""
start_at = 0
max_results = 50
all_issues = []
while True:
    issues = jira.search_issues(
        jql_query,
        startAt=start_at,
        maxResults=max_results,
        fields="summary,status,assignee,created"
    )

    if not issues:
        break

    for issue in issues:
        all_issues.append({
            "Key": issue.key,
            "Summary": issue.fields.summary,
            "Status": issue.fields.status.name,
            "Assignee": issue.fields.assignee.displayName if issue.fields.assignee else None,
            "Created": issue.fields.created
        })

    start_at += len(issues)

# Conversion en DataFrame
df = pd.DataFrame(all_issues)

# Export en CSV
df.to_csv("jira_issues.csv", index=False, encoding="utf-8")

print("✅ Export terminé : jira_issues.csv")