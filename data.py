from dataclasses import dataclass
expected_title = "Чтобы разместить объявление, авторизуйтесь"
# Класс с URL
@dataclass(frozen=True)
class Urls:
    #url учебного сервиса Доска
    BASE: str = 'https://qa-desk.stand.praktikum-services.ru/'

@dataclass
class RegData:
    email: str
    password: str

# Класс с тестовыми пользователями
@dataclass
class TestUsers:
    # email и пароль заранее созданного пользователя
    VALID_USER = RegData(email="tester3@mail.ru", password="123")
    INVALID_USER = RegData(email="invalid", password="invalid")

# данные для ввода объявления
@dataclass
class AdData:
    title: str
    description: str
    price: str
    city: str = "Москва"

# Готовые экземпляры для тестов
TEST_AD = AdData(title="Объявление", description="Описание в объявлении", price="15000")
URL = Urls.BASE
