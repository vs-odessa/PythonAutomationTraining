import requests
import api.jira_endpoints as jira_endpoints
from functions.data_helper import encode_to_base64, is_json
from api.jira_api_client import jira_get_request, jira_post_request, jira_put_request, get_response_type, ResponseType
import random
import allure

_base_url = "https://jira.hillel.it/rest"
_username = "VolodymyrStepanov"
_password = "VolodymyrStepanov"
_headers = {'Content-Type': 'application/json'}


def get_full_url(endpoint_path, base_url=_base_url):
    return base_url + endpoint_path


@allure.title('Login to Jira')
def login(username=_username, password=_password):
    full_url = get_full_url(jira_endpoints.login)
    auth_data = {"username": username, "password": password}
    response = requests.post(full_url, json=auth_data, headers=_headers)
    return response


def login_succeeded(response_to_check):
    if response_to_check.status_code is 200:
        return True
    return False


def add_auth_header(headers, username=_username, password=_password):
    credentials = username + ":" + password
    encoded_credentials = encode_to_base64(credentials)
    headers['Authorization'] = "Basic " + encoded_credentials
    return headers


def get_session_id(username=_username, password=_password):
    response = login(username, password)
    if response.status_code is 200:
        response_json = response.json()
        token = response_json["session"]["value"]
        if len(token) >= 0:
            return token
    else:
        return "Session is not established"


@allure.step('Create Jira Issue')
def create_issue(project_key, issue_type="Bug", summary="", description=""):
    full_url = get_full_url(jira_endpoints.create_issue)
    issue_body = {
        "fields": {
            "project":
                {
                    "key": ""
                },
            "summary": "",
            "description": "",
            "issuetype": {
                "name": ""
                }
        }
    }

    issue_body_timetracking = {
        "fields": {
            "project":
                {
                    "key": ""
                },
            "summary": "",
            "description": "",
            "issuetype": {
                "name": ""
            },
            "timetracking": {
                "originalEstimate": "1d 12h",
                "remainingEstimate": "2h 30m"
            }
        }
    }

    issue_body["fields"]["project"]["key"] = project_key
    issue_body["fields"]["summary"] = summary
    issue_body["fields"]["description"] = description
    issue_body["fields"]["issuetype"]["name"] = issue_type

    response = jira_post_request(full_url, issue_body)
    return response


def issue_created(response_to_check):
    if response_to_check.status_code is 201:
        return True
    return False



def check_if_valid_json_response(response):
    if get_response_type(response) != ResponseType.SUCCESS:
        return "Request is not successful: " + str(response.status_code)
    if not response.json():
        return "Response is not a valid json"


def check_if_valid_error_response(response):
    if get_response_type(response) != ResponseType.CLIENT_ERROR:
        return "Request is not successful: " + str(response.status_code)
    if not response.json():
        return "Response is not a valid json"


def get_error_summary(response):
    check_if_valid_error_response(response)
    try:
        response_json = response.json()
        error_summary = response_json["errors"]["summary"]
        return error_summary
    except Exception:
        return "JSON response has no expected key"


@allure.step('Search Jira Issue')
def search_issues(**search_params):
    params = dict()
    for key, value in search_params.items():
        params[key] = value
    full_url = get_full_url(jira_endpoints.search_issue)
    response = jira_get_request(full_url, params)
    return response


def get_issue_key(result_response):
    response_json = result_response.json()
    issue_key = response_json["issues"][0]["key"]
    return issue_key


def get_issue_info_by_key(issue_key):
    full_url = get_full_url(jira_endpoints.create_issue) + "/" + issue_key
    issue = jira_get_request(full_url)
    return issue


@allure.step('Update Jira Issue')
def update_issue(issue_key, **fields_to_update):
    full_url = get_full_url(jira_endpoints.create_issue) + "/" + issue_key
    fields = dict()
    for key, value in fields_to_update.items():
        fields[key] = value
    update_body = {"fields": fields}
    response = jira_put_request(full_url, update_body)
    return response


@allure.step('Update Jira Issue Priority')
def update_issue_priority(issue_key, new_priority):
    full_url = get_full_url(jira_endpoints.create_issue) + "/" + issue_key
    update_body = {"update": {"priority": [{"set": {"name": new_priority}}]}}
    response = jira_put_request(full_url, update_body)
    return response


@allure.step('Update Jira Issue Assignee')
def update_issue_assignee(issue_key, new_assignee):
    full_url = get_full_url(jira_endpoints.create_issue) + "/" + issue_key
    update_body = {"fields": {"assignee": {"name": new_assignee}}}
    response = jira_put_request(full_url, update_body)
    return response


def get_random_priority():
    list_priorities = ["Normal", "Lowest", "Low", "Medium", "High", "Highest", "Blocker"]
    return random.choice(list_priorities)
