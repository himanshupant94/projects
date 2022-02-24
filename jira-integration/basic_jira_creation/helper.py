from jira import JIRA


class JiraHelper:

    def __init__(self, username, password, server):
        self.jira = JIRA(options={"server": server, "verify":False},basic_auth=(username, password))

    def create_issue(self, test_data):
        issue_key = self.jira.create_issue(fields=test_data)
        return issue_key