from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import data_for_registration
from locators import TestLocators
import data


class TestUserRegistration:

    def _register_new_user(self, driver):
        driver.get(data.URL)
        # cгенерировали email и password
        user = data_for_registration()
        # Ожидать загрузку страницы и нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (TestLocators.LOGIN_BUTTON)).click()
        # ожидать загрузку страницы и нажать кнопку «Нет аккаунта».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (TestLocators.NO_ACCOUNT_BUTTON)).click()
        # Заполнить все поля формы регистрации
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(user.email)
        # Заполнить пароль
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(user.password)
        # Заполнить повторный пароль
        driver.find_element(*TestLocators.SUBMIT_PSW_INPUT).send_keys(user.password)
        # нажать кнопку «Создать аккаунт».
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable
            (TestLocators.CREATE_ACCOUNT_BUTTON)).click()


        #Проверить: произошёл переход на главную страницу, в правом верхнем углу
        # около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        # Проверить Кнопка «Разместить объявление» присутствует
    def test_place_advertisement_button_displayed_after_registration(self, driver):
        #Проверяет, что кнопка «Разместить объявление» отображается после успешной регистрации
        self._register_new_user(driver)

        place_ad_btn = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located
            (TestLocators.PLACE_ADVERTISEMENT_BUTTON))
        assert place_ad_btn.is_displayed(), "Кнопка 'Разместить объявление' не отображается"

    def  test_avatar_button_displayed_after_registration(self, driver):
        #Проверяет, что кнопка аватара отображается после успешной регистрации
        self._register_new_user(driver)
        avatar_button = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located
            (TestLocators.AVATAR_BUTTON))
        assert avatar_button.is_displayed(), "Кнопка аватара не отображается"

    def test_user_name_displayed_after_registration(self, driver):
        #Проверяет, что имя пользователя 'User.' отображается после успешной регистрации
        self._register_new_user(driver)
        user_name_element = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located
            (TestLocators.USER_NAME))
        assert user_name_element.text.strip() == "User.", f"Ожидалось 'User.', получено: '{user_name_element.text}'"
