
import pytest 
import requests as r
import allure
from urls import URLs
from helpers import GenerateTestData, GererationDataRegistration
from data import TestDataRegistration

class TestCreateCourier:
    @allure.title('Тест успешной регистрации курьера')
    def test_create_courier_account_successful(self):

        with allure.step('Вызов post-метода регистрации курьера'):
            response = r.post(URLs.CREATE_COURIER, data=GenerateTestData.data)
        with allure.step('Проверка статус кода и тела ответа'):
            assert response.status_code == 201 and response.json() == TestDataRegistration.RETURN_STATUS_CODE_201

    
    @allure.title('Тест недопустимости создания курьера с уже существующими логином и паролем')
    def test_create_courier_account_duplicate(self):

        with allure.step('Вызов post-метода регистрации пользователя с известными log-pass в теле'):
            response = r.post(URLs.CREATE_COURIER, data=GererationDataRegistration.data)
        with allure.step('Проверка статус кода и тела ответа'):
            assert response.status_code == 409 and response.json() == TestDataRegistration.RETURN_STATUS_CODE_409

        
    
    @pytest.mark.parametrize('data_without_required_fields', 
                             [GenerateTestData.data_without_login, 
                              GenerateTestData.data_without_password, 
                              GenerateTestData.data_without_login_and_password])
    @allure.title('Тест недопустимости создания курьера без обязателельных параметров в теле запроса')
    def test_create_courier_account_without_required_fields(self, data_without_required_fields):
        
        with allure.step('Вызов post-метода регистрации курьера без передачи обязательных параметров в теле запроса'):
            response = r.post(URLs.CREATE_COURIER, data=data_without_required_fields)
        with allure.step('Проверка статус кода и тела ответа'):
            assert response.status_code == 400 and response.json() == TestDataRegistration.RETURN_STATUS_CODE_400


