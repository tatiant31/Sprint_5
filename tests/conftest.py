import pytest
from selenium import webdriver
from faker import Faker


#запуск webdriver
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

#генерация email и пароля
@pytest.fixture(scope="function")
def data_for_registration():
    fake = Faker()
    return {
        'email': fake.email(),
        'password': fake.password(length=12),
       }