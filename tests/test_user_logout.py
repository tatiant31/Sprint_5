from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from helpers import login_and_logout

class TestUserLogout:
    def test_avatar_hidden_after_logout(self, driver):
        login_and_logout(driver)
        # Проверить аватар пользователя больше не отображается
        WebDriverWait(driver, 5).until_not(
            expected_conditions.presence_of_element_located(TestLocators.AVATAR_BUTTON))
        assert len(driver.find_elements(*TestLocators.AVATAR_BUTTON)) == 0

    def test_username_hidden_after_logout(self, driver):
        login_and_logout(driver)
        # Проверить  имя User больше не отображается
        WebDriverWait(driver, 5).until_not(
            expected_conditions.presence_of_element_located(TestLocators.USER_NAME))
        assert len(driver.find_elements(*TestLocators.USER_NAME)) == 0

    def test_login_button_visible_after_logout(self, driver):
        login_and_logout(driver)
        # Проверить отображение кнопки «Вход и регистрация»
        login_button = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
        assert login_button.is_displayed()

    def test_place_ad_button_visible_after_logout(self, driver):
        login_and_logout(driver)
        #кнопка Разместить объявление осталась
        place_ad_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.PLACE_ADVERTISEMENT_BUTTON))
        assert place_ad_button.is_displayed()



