import sys
sys.path.append('.')
import api.jira_actions as jira
from functions.data_helper import generate_random_string


class TestCreateIssuesApi:

    def test_create_issue_positive(self):
        project_key = "WEBINAR"
        issue_type = "Bug"
        issue_summary = "Created from API"
        issue_description = "Created with API using project key"
        response = jira.create_issue(project_key, issue_type, issue_summary, issue_description)
        assert jira.issue_created(response)

    def test_create_issue_empty_summary(self):
        project_key = "WEBINAR"
        issue_type = "Bug"
        issue_summary = ""
        issue_description = "Created with API using project key"
        response = jira.create_issue(project_key, issue_type, issue_summary, issue_description)
        assert response.status_code == 400
        expected_error_message = "You must specify a summary of the issue."
        assert jira.get_error_summary(response) == expected_error_message

    def test_create_issue_summary_exceeded_length(self):
        project_key = "WEBINAR"
        issue_type = "Bug"
        issue_summary = generate_random_string(256)
        issue_description = "Created with API using project key"
        response = jira.create_issue(project_key, issue_type, issue_summary, issue_description)
        assert response.status_code == 400
        expected_error_message = "Summary must be less than 255 characters."
        assert jira.get_error_summary(response) == expected_error_message
