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
        # заголовок «Чтобы разместить объявление, авторизуйтесь»
        modal_title = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located
            (TestLocators.PLACE_ADVERTISEMENT_TEXT))
        # Проверяем, что элемент с заголовком отображается
        assert modal_title.is_displayed(), "Заголовок модального окна не отображается"

