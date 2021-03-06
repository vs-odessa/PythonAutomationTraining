import base64
import random
import string
import json
import datetime


def encode_to_base64(string_to_encode):
    encoded = base64.b64encode(bytes(string_to_encode, 'utf-8')).decode('utf-8')
    return encoded


def get_current_timestamp_string():
    datetime_formatted = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return datetime_formatted


def generate_random_string(str_length):
    return ''.join(random.choice(string.ascii_lowercase + ' ') for i in range(str_length))


def is_json(obj):
    try:
        json_object = json.loads(obj)
    except ValueError:
        return False
    return True
