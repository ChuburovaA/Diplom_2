import requests
import allure
import pytest

from conftest import *
from data import *


@allure.story('Тесты на логин пользователя')
class TestLoginUser:

    @allure.title('Успешная авторизация пользователя')
    def test_login_user_correct(self, create_and_delete_user):
        response = requests.post(Urls.login, data=create_and_delete_user[2])

        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title('Не успешная авторизация пользователя при невернно введеном логине и/или пароле')
    @pytest.mark.parametrize('payload',
                             [
                                 {'email': f'{generate_random_string(5)}@yandex.ru'},
                                 {'password': generate_random_string(5)}
                             ]
                             )
    def test_login_user_incorrect(self, create_and_delete_user, payload):
        response = requests.post(Urls.login, data=payload)

        assert response.status_code == 401 and response.json()['message'] == ErrorMessages.incorrect_login
