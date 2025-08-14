
import pytest
import requests as r
import allure
from urls import URLs
from data import TestDataAuthorization
from helpers import GenerateTestData, GenerationDataAuthorization

class TestLoginCourier:

    @allure.title('Тест успешной авторизации курьера')
    def test_login_courier_successful(self):

        with allure.step('Вызов post-метода для авторизации курьера с валидными данными в теле'):
            response = r.post(URLs.LOGIN_COURIER, data=GenerationDataAuthorization.data_for_login)
        with allure.step('Проверка статус кода и тела возваращения в теле id курьера'):
            assert response.status_code == 200 and 'id' in response.text 


    
    @pytest.mark.parametrize('login_with_empty_login_and_password', [GenerateTestData.data_with_empty_login, 
                                                                     GenerateTestData.data_with_empty_password,
                                                                     GenerateTestData.data_with_empty_login_and_password])
    @allure.title('Тест недопустимости авторизации без передачи логина и(или) пароля курьера')
    def test_login_courier_with_empty_login_and_password(self,login_with_empty_login_and_password):

        with allure.step('Вызов post-метода авторизации курьера без логина/пароля в теле'):
            response = r.post(URLs.LOGIN_COURIER, json=login_with_empty_login_and_password)
        with allure.step('Проверка статус кода и тела ответа'):
            assert response.status_code == 400 and response.json() == TestDataAuthorization.RETURN_STATUS_CODE_400

    @allure.title('Тест недопустимости авторизации курьера с неизвестными логином и паролем')
    def test_login_courier_unknow_login_and_password(self):
        with allure.step('Вызов post-метода авторизации курьера с неизвестными логином и паролем в теле'):
            response = r.post(URLs.LOGIN_COURIER, data=TestDataAuthorization.UNKNOW_LOGIN_AND_PASSWORD)
        with allure.step('Проверка статуса кода и тела ответа'):
            assert response.status_code == 404 and response.json() == TestDataAuthorization.RETURN_STATUS_CODE_404

            