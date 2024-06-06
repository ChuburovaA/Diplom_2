class Urls:

    BASE_URL = 'https://stellarburgers.nomoreparties.site/api'
    register = BASE_URL + '/auth/register'
    user_data = BASE_URL + '/auth/user'
    login = BASE_URL + '/auth/login'
    orders = BASE_URL + '/orders'
    ingredients = BASE_URL + '/ingredients'

class ErrorMessages:
    user_is_create = 'User already exists'
    incorrect_user_data = 'Email, password and name are required fields'
    ingredients_without_id_in_order = 'Ingredient ids must be provided'
    incorrect_login = "email or password are incorrect"
    internal_server_error = 'Internal Server Error'
    unauthorized = 'You should be authorised'


class IngredientsData:
    correct_ingredients = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa73"
        ]
    }
    incorrect_ingredients = {
        "ingredients": [
            "61c@#$71d1f812fgdaaa69",
            "61c0c1d1f***8yhfbdaaa6k"
        ]
    }