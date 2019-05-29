import api.jira_actions as jira_lib

_username = "VolodymyrStepanov"
_password = "VolodymyrStepanov"


class TestLoginJiraApi:

    def test_login_api_positive(self):
        response = jira_lib.login(_username, _password)
        assert jira_lib.login_succeeded(response)

    def test_get_session(self):
        token = jira_lib.get_session_id(_username, _password)
        assert token is not None

