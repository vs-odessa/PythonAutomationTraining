import sys
sys.path.append('.')
import api.jira_actions as jira
from functions.data_helper import generate_random_string
import allure


class TestUpdateIssuesApi:

    @allure.tag('api')
    @allure.title('Update Jira Issue description')
    def test_update_issue_description(self):
        my_issue = jira.search_issues(jql="assignee=VolodymyrStepanov")
        new_description = "Description was updated with:" + generate_random_string(10)
        my_issue_key = jira.get_issue_key(my_issue)

        response = jira.update_issue(my_issue_key, description=new_description)
        assert response.status_code == 204
        updated_issue = jira.get_issue_info_by_key(my_issue_key)
        assert updated_issue.json()["fields"]["description"] == new_description

    @allure.tag('api')
    @allure.title('Update Jira Issue Priority')
    def test_update_issue_priority(self):
        my_issue = jira.search_issues(jql="assignee=VolodymyrStepanov")
        my_issue_key = jira.get_issue_key(my_issue)
        new_priority = jira.get_random_priority()

        response = jira.update_issue_priority(my_issue_key, new_priority)
        assert response.status_code == 204
        updated_issue = jira.get_issue_info_by_key(my_issue_key)
        assert updated_issue.json()["fields"]["priority"]["name"] == new_priority

    @allure.tag('api')
    @allure.title('Update Jira Issue Assignee')
    def test_update_issue_assignee(self):
        old_assignee="VolodymyrStepanov"
        new_assignee = ""
        my_issue = jira.search_issues(jql="assignee="+old_assignee)
        my_issue_key = jira.get_issue_key(my_issue)
        response = jira.update_issue_assignee(my_issue_key, new_assignee)
        assert response.status_code == 204
        updated_issue = jira.get_issue_info_by_key(my_issue_key)
        assert updated_issue.json()["fields"]["assignee"] == None
        # cleanup
        jira.update_issue_assignee(my_issue_key, old_assignee)



