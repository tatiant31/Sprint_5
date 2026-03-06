from faker import Faker
from data import RegData

fake = Faker('en_US')

# генерация email и пароля
def data_for_registration() -> RegData:
    #Возвращает объект RegData с фейковыми данными
    return RegData(
        email=fake.email(),
        password=fake.password(length=12)
    )