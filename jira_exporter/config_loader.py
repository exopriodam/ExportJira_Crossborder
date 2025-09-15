import os, sys, json

def get_base_dir():
    if getattr(sys, 'frozen', False):   # running as .exe
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

BASE_DIR = get_base_dir()
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

JIRA_URL = config["jira"]["url"]
JIRA_USER = config["jira"]["user"]
JIRA_TOKEN = config["jira"]["token"]
JIRA_JQL = config["jira"]["JQL"]
DATE_TO_USE_START = config["jira"]["date_start"]
DATE_TO_USE_END = config["jira"]["date_end"]
DEFAULT_FIELDS = config["jira"]["format"]
