import allure
import requests

from methods import Methods
from data import Urls

@allure.title('Проверка авторизации курьера с разными данными')
@pytest.mark.parametrize('login, password, expected_status, expected_message', [
    ('', 'password', 400, "Недостаточно данных для входа"),
    ('login', '', 400, "Недостаточно данных для входа"),
    ('&*#^$(*&^#$', '*(&$TRYGF*(G#(F*#&^T', 404, "Учетная запись не найдена")
])
def test_login_courier_with_different_data(login, password, expected_status, expected_message, create_courier):
    methods = Methods()
    req = methods.register_new_courier_and_return_login_password()
    requests.post(Urls.CREATE_COURIER, data=req)
    del req['firstName']
    req['login'] = login
    req['password'] = password
    response = requests.post(Urls.LOGIN, data=req)

    assert response.status_code == expected_status
    assert response.json()['message'] == expected_message
