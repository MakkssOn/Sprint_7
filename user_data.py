class TextMessages:
    OK_CREATE = '{"ok":true}'
    LOGIN_BUSY = "Этот логин уже используется. Попробуйте другой."
    INSUFFICIENT_DATA = "Недостаточно данных для создания учетной записи"

    person_data = [
        ['Тёма', 'Топазов', 'Советский проспект, 16', '7', '+79005673465', '5', '2024-09-20',
         'Поскорее бы', "BLACK"],
        ['Lil', 'Peepers', 'Ул. Карла Маркса', '4', '+79954542288', '7', '2024-09-20',
         'Розовый самый лучший', "GREY"],
        ['Bayerische', 'Benzo', 'Bayern', '77', '+79999882277', '9', '2024-09-20',
         'С удовольствием за рулём', "BLACK, GREY"],
        ['Katsumi', 'Uchiha', 'Japan .', '20', '+89564646467', '3', '2024-09-20',
         'Единственный, кто может меня победить — это я сам!', ""]
    ]


class Urls:
    CREATE_ORDERS = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    CREATE_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    RECEIVING_ORDERS = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    LOGIN = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    DELETE_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'



