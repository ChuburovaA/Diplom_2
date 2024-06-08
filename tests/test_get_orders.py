import allure
import requests

from conftest import *
from data import *

@allure.story('Тесты на получение заказов конкретного пользователя')
class TestGetOrders:

    @allure.title('Заказ выполненный авторизированным пользователем')
    def test_get_order_with_auth(self, create_and_delete_user):
        token = {'Authorization': create_and_delete_user[3]}
        requests_create_order = requests.post(Urls.orders, headers=token, data=IngredientsData.correct_ingredients)
        response = requests.get(Urls.orders, headers=token)

        assert response.status_code == 200 and response.json()['orders'][0]['number'] == requests_create_order.json()['order']['number']

    @allure.title('Заказ выполненный н/авторизированным пользователем')
    def test_get_order_without_auth(self, create_and_delete_user):
        response = requests.get(Urls.orders)

        assert response.status_code == 401 and response.json()['message'] == ErrorMessages.unauthorized