from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from data import VALID_USER
from locators import TestLocators

class TestUserLogin:
    def _login_user(self, driver):
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

        #Проверить: произошёл переход на главную страницу, в правом верхнем углу
        #около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        # Проверить Кнопка «Разместить объявление» присутствует
    def test_place_advertisement_button_is_displayed_after_login(self, driver):
        self._login_user(driver)
        place_ad_btn = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located
            (TestLocators.PLACE_ADVERTISEMENT_BUTTON))
        assert place_ad_btn.is_displayed(), "Кнопка 'Разместить объявление' не отображается"

    def test_avatar_button_is_displayed_after_login(self, driver):
        self._login_user(driver)
        # Проверить кнопку аватара (circleSmall) - она есть на главной странице
        avatar_button = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located
            (TestLocators.AVATAR_BUTTON))
        assert avatar_button.is_displayed(), "Кнопка аватара (circleSmall) не отображается"

    def test_user_name_is_correct_after_login(self, driver):
        self._login_user(driver)
        # Проверить в правом верхнем углу отображается аватар и имя "User"
        user_name_element = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                TestLocators.USER_NAME))
        assert user_name_element.text.strip() == "User.", f"Ожидалось 'User.', получено: '{user_name_element.text}'"


