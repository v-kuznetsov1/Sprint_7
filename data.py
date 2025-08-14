
class TestDataRegistration:
     
    RETURN_STATUS_CODE_409 = {
        "code": 409,
        "message": "Этот логин уже используется. Попробуйте другой."
        }
    
    RETURN_STATUS_CODE_400 = {
        "code": 400,
        "message": "Недостаточно данных для создания учетной записи"
        }
    
    RETURN_STATUS_CODE_201 = {"ok": True}



class TestDataAuthorization:
   
    UNKNOW_LOGIN_AND_PASSWORD = {
            "login": 'fef3434fefefe',
            "password": 'efef42343ff'
            }
    
    RETURN_STATUS_CODE_400 = {
        "code": 400,
        "message": "Недостаточно данных для входа"
        }
    
    RETURN_STATUS_CODE_404 = {
        "code": 404,
        "message": "Учетная запись не найдена"
        }
    

class TestDataCreateOrder:

    data_for_create_order = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
        }
    


class TestDataReturnOrderList:

    orders = ["orders", "id", "courierId", "firstName", 
              "lastName", "address", "metroStation", "phone", "rentTime", 
              "deliveryDate", "track", "color", "comment", "createdAt", "updatedAt", "status"]
    
