import api.jira_actions as jira
import allure

class TestSearchIssuesApi:

    @allure.tag('api')
    @allure.title('Search Jira Issue by Assignee')
    def test_search_issue_by_assignee(self):
        response = jira.search_issues(jql="assignee=VolodymyrStepanov")
        with allure.step('Check search result'):
            assert response.json()["issues"][0]["fields"]["assignee"]["name"] == "VolodymyrStepanov"

    @allure.tag('api')
    @allure.title('Search Jira Issue with limit')
    def test_search_issue_limit_search(self):
        response = jira.search_issues(jql="assignee=VolodymyrStepanov", startAt="1", maxResults="5")
        result_count = len(response.json()["issues"])
        with allure.step('Check search result'):
            assert result_count == 5

    @allure.tag('api')
    @allure.title('Search Jira Issue with no Result')
    def test_search_issue_no_result(self):
        response = jira.search_issues(jql="assignee=NonExistingUser")
        with allure.step('Check search result'):
            assert response.json()["total"] == 0
