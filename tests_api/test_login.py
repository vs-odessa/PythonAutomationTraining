import sys
sys.path.append('.')
import api.jira_actions as jira_lib
import allure
import pytest


_username = "VolodymyrStepanov"
_password = "VolodymyrStepanov"


@pytest.mark.api
class TestLoginJiraApi:

    @allure.tag('api')
    @allure.title('Login to Jira - Positive')
    def test_login_api_positive(self):
        response = jira_lib.login(_username, _password)
        assert jira_lib.login_succeeded(response)

    @allure.tag('api')
    @allure.title('Get Session ID')
    def test_get_session(self):
        token = jira_lib.get_session_id(_username, _password)
        assert token is not None

