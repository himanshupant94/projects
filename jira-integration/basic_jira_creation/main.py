from helper import JiraHelper
import os

username = os.environ.get("username")
password = os.environ.get("password")
server = os.environ.get("server")
jira = JiraHelper(username, password, server)

# Test Data for Creating Issue
test_data = {
    "project": "DWO",
    "summary": "Ops-Analytics Cloud DAG failed",
    "description": "test_description",
    "issuetype": {"name": "Job Failure"}
}

# Creating Test in Jira
jira.create_issue(test_data)
