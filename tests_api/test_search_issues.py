import api.jira_actions as jira


class TestSearchIssuesApi:

    def test_search_issue_by_assignee(self):
        response = jira.search_issues(jql="assignee=VolodymyrStepanov")
        assert response.json()["issues"][0]["fields"]["assignee"]["name"] == "VolodymyrStepanov"

    def test_search_issue_limit_search(self):
        response = jira.search_issues(jql="assignee=VolodymyrStepanov", startAt="1", maxResults="5")
        result_count = len(response.json()["issues"])
        assert result_count == 5

    def test_search_issue_no_result(self):
        response = jira.search_issues(jql="assignee=NonExistingUser")
        assert response.json()["total"] == 0
