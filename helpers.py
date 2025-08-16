
import requests
import random
import string
from faker import Faker


class GenerateTestData:
    
    fake = Faker()
    
    login = fake.user_name()
    password = fake.password(length=8, digits=True)
    first_name = fake.first_name()
    
    data = {
            "login": login,
            "password": password,
            "firstName": first_name
            }
    
    data_without_login = {
            "password": password
            }
    
    data_without_password = {
            "login": login
            }
    
    data_without_login_and_password = {}
    
    
    data_with_empty_login = {
            "login": "",
            "password": password
            }
    
    data_with_empty_password = {
            "login": login,
            "password": ""
            }
    
    data_with_empty_login_and_password = {
            "login": "",
            "password": ""
            }

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass 


class GererationDataRegistration:
    
    test_data = register_new_courier_and_return_login_password()
    data = {
        "login": test_data[0],
        "password": test_data[1],
        "firstName": test_data[2]
        }
    

class GenerationDataAuthorization:

    test_data = register_new_courier_and_return_login_password()
    data_for_login = {
        "login": test_data[0],
        "password": test_data[1]
        }
   