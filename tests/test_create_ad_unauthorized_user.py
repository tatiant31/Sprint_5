from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from locators import TestLocators

class TestCreateAdUnauthorizedUser():
    def test_create_ad_unauthorized_user(self, driver):
        driver.get(data.URL)
        # Ожидать загрузку страницы и нажать кнопку «Разместить объявление».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (TestLocators.PLACE_ADVERTISEMENT_BUTTON)).click()
        # заголовком «Чтобы разместить объявление, авторизуйтесь»
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located
            (TestLocators.WINDOW_ADVERTISEMENT))
        # заголовок «Чтобы разместить объявление, авторизуйтесь»
        modal_title = driver.find_element(*TestLocators.WINDOW_TITLE)
        modal_title = driver.find_element(*TestLocators.WINDOW_TITLE)
        assert modal_title.text == "Чтобы разместить объявление, авторизуйтесь", \
            "Неправильный заголовок модального окна"

