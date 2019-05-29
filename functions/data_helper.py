import base64
import random
import string


def encode_to_base64(string_to_encode):
    encoded = base64.b64encode(bytes(string_to_encode, 'utf-8')).decode('utf-8')
    return encoded


def generate_random_string(str_length):
    return ''.join(random.choice(string.ascii_lowercase + ' ') for i in range(str_length))
