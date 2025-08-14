
import requests as r
import pytest
import allure
from data import TestDataCreateOrder
from urls import URLs


class TestCreateOrder:

    @pytest.mark.parametrize('color_option', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    @allure.title('Тест создания заказа с разными вариантами цвета')
    def test_create_order_with_color_options(self, color_option):
        
        with allure.step('Генерация тела запроса с различными вариантами цвета и без него'):
            color_option = TestDataCreateOrder.data_for_create_order['color'] = color_option
        with allure.step('Вызов post-метода регистрации заказа'):
            response = r.post(URLs.ORDER, json=color_option)
        with allure.step("Проверка статус кода и возвращения в теле track'a заказа"):
            assert response.status_code == 201 and 'track' in response.text

    