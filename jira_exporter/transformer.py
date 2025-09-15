class IssueTransformer:
    @staticmethod
    def transform(issue):
        return {
            "Key": issue.key,
            "ID": issue.id,
            "Summary": issue.fields.summary,
            "Status": issue.fields.status.name,
            "Assignee": issue.fields.assignee.displayName if issue.fields.assignee else None,
            "Created": issue.fields.created,
            "System Number": getattr(issue.fields, "customfield_10828", None)
        }
