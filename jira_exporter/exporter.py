import pandas as pd

class Exporter:
    def export(self, data):
        raise NotImplementedError

class CsvExporter(Exporter):
    def __init__(self, filename="jira_issues.csv"):
        self.filename = filename

    def export(self, data):
        df = pd.DataFrame(data)
        df.to_csv(self.filename, index=False, encoding="utf-8")
        return self.filename

class JsonExporter(Exporter):
    def __init__(self, filename="jira_issues.json"):
        self.filename = filename

    def export(self, data):
        import json
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return self.filename

class XlsxExporter(Exporter):
    def __init__(self, filename="jira_issues.xlsx"):
        self.filename = filename

    def export(self, data):
        df = pd.DataFrame(data)
        df.to_excel(self.filename, index=False, engine="openpyxl")
        return self.filename