from __future__ import annotations
import re
from jira import JIRA
#os.environ["HTTPS_PROXY"]="https://10.235.1.14:8080"
#os.environ["HTTP_PROXY"]="http://10.235.1.14:8080"


#file = "config.json"
#config = json.load(open(file))
jira = JIRA(server="https://it-projects.just.fgov.be/",
                       basic_auth=("svcshrcrossdev01@just.fgov.be", "fa$tLemur37"),
                       validate=True,
                       proxies={"http": "http://10.235.1.14:8080", "https": "http://10.235.1.14:8080"})
issues_in_proj = jira.search_issues('project=BOT')
for issue in jira.search_issues('project = BOT AND status = Pending'):
    print('{}: {}'.format(issue.key, issue.fields.summary))
# LOGIN(user="svcshrcrossdev01@just.fgov.be",password="fa$tLemur37",url="https://it-projects.just.fgov.be/")
# jql = "project in (BOT) order by created DESC"
# issue_export(jql=jql, extension="json")