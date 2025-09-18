from datetime import datetime

class IssueTransformer:
    @staticmethod
    def transform(issue):

        return {
            "Key": issue.key,
            "ID": issue.id,
            "Created": datetime.strptime(issue.fields.created,"%Y-%m-%dT%H:%M:%S.%f%z").strftime("%d-%m-%Y"),
            "Status": issue.fields.status.name,
            "Updated": datetime.strptime(issue.fields.updated,"%Y-%m-%dT%H:%M:%S.%f%z").strftime("%d-%m-%Y"),
            "Assignee": issue.fields.assignee.displayName if issue.fields.assignee else None,
            "Component/s": issue.fields.components[0]if issue.fields.components else None,
            "Component/s_1": "",
            "Custom field (Source)":getattr(issue.fields, "customfield_10835",None),
            "Qualification": getattr(issue.fields, "customfield_11103", None)

        }
        # return True