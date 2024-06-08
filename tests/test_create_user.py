import requests
import allure
import pytest

from data import *
from conftest import *

@allure.story('Тесты на создание пользователя')
class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_new_user(self, create_user_data):
        payload = create_user_data
        response = requests.post(Urls.register, data=payload)

        assert response.status_code == 200 and response.json().get('success') is True

    @allure.title('Повторная регистрация пользователя')
    def test_create_used_user(self, create_user_data, create_and_delete_user):
        response = requests.post(Urls.register, data=create_and_delete_user[1])

        assert response.status_code == 403 and response.json()['message'] == ErrorMessages.user_is_create


    @allure.title('Регистрация курьера без обязательных полей')
    def test_create_user_without_required_fields(self, create_user_data, create_and_delete_user):
        payload = create_user_data
        del payload['email']
        response = requests.post(Urls.register, data=payload)

        assert response.status_code == 403 and response.json().get('message') == ErrorMessages.incorrect_user_data