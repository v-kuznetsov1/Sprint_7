
import requests as r
import allure
from urls import URLs
from data import TestDataReturnOrderList

class TestOrderList:
    @allure.title('Тест метода, возвращающего список заказов')
    def test_return_order_list(self):
        with allure.step('Вызов get-метод, возвращающего список заказов'):
            response = r.get(URLs.ORDER)
        with allure.step('Проверка статус кода ответа'):
            assert response.status_code == 200
        with allure.step('Проверка возварщения в теле ответа списка заказов со всеми параметрами'):
            for key in TestDataReturnOrderList.orders:
                assert key in response.text, f'response body не содержит ожидаемый параметр {key}'

