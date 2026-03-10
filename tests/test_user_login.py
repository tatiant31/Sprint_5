from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from helpers import login_user
import data

class TestUserLogin:
    # Проверить Кнопка «Разместить объявление» присутствует
    def test_place_advertisement_button_is_displayed_after_login(self, driver):
        driver.get(data.URL)
        login_user(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located
            (TestLocators.PLACE_ADVERTISEMENT_BUTTON))
        assert True, "Кнопка 'Разместить объявление' отображается после входа"

    def test_avatar_button_is_displayed_after_login(self, driver):
        driver.get(data.URL)
        login_user(driver)
        # Проверить кнопку аватара есть на главной странице
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located
            (TestLocators.AVATAR_BUTTON))
        assert True, "Кнопка аватара отображается после входа"

    def test_user_name_is_correct_after_login(self, driver):
        driver.get(data.URL)
        login_user(driver)
        # Проверить в правом верхнем углу отображается аватар и имя "User"
        user_name_element = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.USER_NAME))
        assert user_name_element.text.strip() == "User.", f"Ожидалось 'User.', получено: '{user_name_element.text}'"


