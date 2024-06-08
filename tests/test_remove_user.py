import pytest
import allure
import requests

from data import *
from conftest import *

@allure.story('Тесты на изменение данных пользователя')
class TestChangeUser:

    @allure.title('Изменение почты у авторизированного пользователя')
    def test_change_user_email(self, create_and_delete_user):
        new_email = f'{generate_random_string(6)}yandex.ru'
        payload = {'email': new_email}
        token = {'Authorization': create_and_delete_user[3]}
        response = requests.patch(Urls.user_data, headers=token, data=payload)

        assert response.status_code == 200 and response.json()['user']['email'] == new_email

    @allure.title('Изменение пароля у авторизированного пользователя')
    def test_change_user_password(self, create_and_delete_user):
        new_password = generate_random_string(6)
        payload = {'password': new_password}
        token = {'Authorization': create_and_delete_user[3]}
        response = requests.patch(Urls.user_data, headers=token, data=payload)

        assert response.status_code == 200 and response.json().get('success') is True

    @allure.title('Изменение имени у авторизированого пользователя')
    def test_change_user_name(self, create_and_delete_user):
        new_name = generate_random_string(6)
        payload = {'name': new_name}
        token = {'Authorization': create_and_delete_user[3]}
        response = requests.patch(Urls.user_data, headers=token, data=payload)

        assert response.status_code == 200 and response.json()['user']['name'] == new_name


    @allure.title('Изменение данных пользователя без аторизации')
    @pytest.mark.parametrize('payload',
                            [
                                {'email': f'{generate_random_string(5)}@yandex.ru'},
                                {'password': generate_random_string(5)},
                                {'name': generate_random_string(5)}
                            ]
    )
    def test_change_user_data_without_authorization_unsuccessful(self, payload):
        response = requests.patch(Urls.user_data, data=payload)
        assert response.status_code == 401 and response.json()['message'] == ErrorMessages.unauthorized