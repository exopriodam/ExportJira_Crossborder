from jira import JIRA
import config

class JiraClient:
    def __init__(self, server=config.JIRA_URL, user=config.JIRA_USER, token=config.JIRA_TOKEN):
        self.jira = JIRA(server=server, basic_auth=(user, token))

    def fetch_issues(self, jql, fields=config.DEFAULT_FIELDS, page_size=50):
        start_at = 0
        while True:
            issues = self.jira.search_issues(jql, startAt=start_at, maxResults=page_size, fields=fields)
            if not issues:
                break
            for issue in issues:
                yield issue
            start_at += len(issues)
