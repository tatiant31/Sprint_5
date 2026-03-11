import pytest
from selenium import webdriver

#запуск webdriver
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

