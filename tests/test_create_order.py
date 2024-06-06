import requests
import allure
import pytest

from data import *
from conftest import *

@allure.story('Тесты на проверку создания заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_if_user_is_auth(self, create_and_delete_user):
        token = {'Authorization': create_and_delete_user[3]}
        response = requests.post(Urls.orders, headers=token, data=IngredientsData.correct_ingredients)

        assert response.status_code == 200 and response.json().get('success') is True

    @allure.title('Создание заказа без авторизации')
    def test_create_order_if_user_is_not_auth(self, create_and_delete_user):
        response = requests.post(Urls.orders, data=IngredientsData.correct_ingredients)

        assert response.status_code == 200 and response.json().get('success') is True

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, create_and_delete_user):
        response = requests.post(Urls.orders)

        assert response.status_code == 400 and response.json()['message'] == ErrorMessages.ingredients_without_id_in_order

    @allure.title('Создание заказа с неверным хэшем ингредиентов')
    def test_create_order_incorrect_hash(self, create_and_delete_user):
        response = requests.post(Urls.orders, data=IngredientsData.incorrect_ingredients)

        assert response.status_code == 500 and ErrorMessages.internal_server_error in response.text