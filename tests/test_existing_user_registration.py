from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from data import VALID_USER
from locators import TestLocators

class TestExistingUserRegistration:
    def _register_existing_user_and_wait_for_errors(self, driver):
        driver.get(data.URL)
        # Ожидать загрузку страницы и нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (TestLocators.LOGIN_BUTTON)).click()
        # ожидать загрузку страницы и нажать кнопку «Нет аккаунта».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (TestLocators.NO_ACCOUNT_BUTTON)).click()
        # Заполнить все поля формы регистрации
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(VALID_USER.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(VALID_USER.password)
        driver.find_element(*TestLocators.SUBMIT_PSW_INPUT).send_keys(VALID_USER.password)
        # нажать кнопку «Создать аккаунт».
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable
            (TestLocators.CREATE_ACCOUNT_BUTTON)).click()
        # Ждем появление ошибки (общий индикатор того, что валидация прошла)
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, ".input_inputError__fLUP9")
            )
        )

    def test_email_field_highlighted_on_existing_user(self, driver):
        self._register_existing_user_and_wait_for_errors(driver)
        # Проверка красной подсветки для поля Email
        email_field = driver.find_element(*TestLocators.EMAIL_RED_FIELD)
        assert "input_inputError__fLUP9" in email_field.get_attribute("class")

    def test_email_error_message_displayed_on_existing_user(self, driver):
        self._register_existing_user_and_wait_for_errors(driver)
        # Проверка сообщения 'Ошибка' под полем Email
        error_message = driver.find_element(*TestLocators.EMAIL_ERROR)
        assert error_message.text == "Ошибка"

    def test_password_field_highlighted_on_existing_user(self, driver):
        self._register_existing_user_and_wait_for_errors(driver)
        # Проверка красной подсветки для поля Пароль
        password_field = driver.find_element(*TestLocators.PASSWORD_RED_FIELD)
        assert "input_inputError__fLUP9" in password_field.get_attribute("class")

    def test_repeat_password_field_highlighted_on_existing_user(self, driver):
        self._register_existing_user_and_wait_for_errors(driver)
        # Проверка красной подсветки для поля Повторите Пароль
        submit_password_field = driver.find_element(*TestLocators.SUBMIT_RED_FIELD)
        assert "input_inputError__fLUP9" in submit_password_field.get_attribute("class")


