from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from data import VALID_USER
from locators import TestLocators

class TestUserLogout:
    def _login_and_logout(self, driver):
        driver.get(data.URL)
        # Ожидать загрузку страницы и нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (TestLocators.LOGIN_BUTTON)).click()
        # Заполняем email
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(VALID_USER.email)
        # Заполнить пароль
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(VALID_USER.password)
        # Нажать кнопку Войти
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(TestLocators.ENTER_BUTTON)).click()
        #Нажать кнопку Выйти
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)).click()

    def test_avatar_hidden_after_logout(self, driver):
        self._login_and_logout(driver)
        # Проверить аватар пользователя больше не отображается
        WebDriverWait(driver, 5).until_not(
            expected_conditions.presence_of_element_located(TestLocators.AVATAR_BUTTON))
        assert len(driver.find_elements(*TestLocators.AVATAR_BUTTON)) == 0

    def test_username_hidden_after_logout(self, driver):
        self._login_and_logout(driver)
        # Проверить  имя User больше не отображается
        WebDriverWait(driver, 5).until_not(
            expected_conditions.presence_of_element_located(TestLocators.USER_NAME))
        assert len(driver.find_elements(*TestLocators.USER_NAME)) == 0

    def test_login_button_visible_after_logout(self, driver):
        self._login_and_logout(driver)
        # Проверить отображение кнопки «Вход и регистрация»
        login_button = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
        assert login_button.is_displayed()

    def test_place_ad_button_visible_after_logout(self, driver):
        self._login_and_logout(driver)
        #кнопка Разместить объявление осталась
        place_ad_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.PLACE_ADVERTISEMENT_BUTTON))
        assert place_ad_button.is_displayed()



