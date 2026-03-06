from dataclasses import dataclass

#url учебного сервиса Доска
URL = 'https://qa-desk.stand.praktikum-services.ru/'

@dataclass
class RegData:
    email: str
    password: str

# данные для ввода объявления
@dataclass
class AdData:
    title: str
    description: str
    price: str
    city: str = "Москва"

# Готовые экземпляры для тестов
# email и пароль заранее созданного пользователя
VALID_USER = RegData(email="tester3@mail.ru", password="123")
INVALID_USER = RegData(email="invalid", password="123")
TEST_AD = AdData(title="Объявление", description="Описание в объявлении", price="15000")
