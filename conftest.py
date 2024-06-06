import pytest
import requests

from helpers import *
from data import *

@pytest.fixture
def create_user_data():
    email = generate_random_string(10) + '@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    return payload

@pytest.fixture(scope="function")
def create_and_delete_user(create_user_data):
    payload = create_user_data
    login_data = payload.copy()
    del login_data["name"]

    response = requests.post(Urls.register, data=payload)
    token = response.json()["accessToken"]

    yield response, payload, login_data, token
    requests.delete(Urls.user_data, headers={'Authorization': f'{token}'})