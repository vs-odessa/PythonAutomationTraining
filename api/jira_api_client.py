import requests
from functions.data_helper import encode_to_base64
from enum import Enum
import http.client as http_client
import logging

_username = "VolodymyrStepanov"
_password = "VolodymyrStepanov"


def encode_credentials():
    credentials = _username + ":" + _password
    return encode_to_base64(credentials)


def set_log_settings():
    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def jira_get_request(url, params=None):
    set_log_settings()
    encoded_credentials = encode_credentials()
    _headers = dict()
    _headers["Authorization"] = "Basic " + encoded_credentials
    _headers["Content-Type"] = "application/json"
    return requests.get(url, params=params, headers=_headers)


def jira_post_request(url, json_body):
    set_log_settings()
    encoded_credentials = encode_credentials()
    _headers = dict()
    _headers["Authorization"] = "Basic " + encoded_credentials
    _headers["Content-Type"] = "application/json"
    return requests.post(url, json=json_body, headers=_headers)


def jira_put_request(url, json_body):
    set_log_settings()
    encoded_credentials = encode_credentials()
    _headers = dict()
    _headers["Authorization"] = "Basic " + encoded_credentials
    _headers["Content-Type"] = "application/json"
    return requests.put(url, json=json_body, headers=_headers)


class ResponseType(Enum):
    UNDEFINED = 0
    INFO = 1
    SUCCESS = 2
    REDIRECTION = 3
    CLIENT_ERROR = 4
    SERVER_ERROR = 5


def get_response_type(response):
    if response.status_code >= 100:
        return ResponseType.INFO
    elif response.status_code >= 200:
        return ResponseType.SUCCESS
    elif response.status_code >= 300:
        return ResponseType.REDIRECTION
    elif response.status_code >= 400:
        return ResponseType.CLIENT_ERROR
    elif 500 <= response.status_code < 600:
        return ResponseType.SERVER_ERROR
    else:
        return ResponseType.UNDEFINED


