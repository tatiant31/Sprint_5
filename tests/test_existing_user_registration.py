from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from helpers import register_existing_user


class TestExistingUserRegistration:

    # Проверка красной подсветки для поля Email
    def test_email_field_highlighted_on_existing_user(self, driver):
        register_existing_user(driver)
        email_field = (WebDriverWait(driver, 10).
            until(expected_conditions.presence_of_element_located
            (TestLocators.EMAIL_RED_FIELD)))
        assert email_field.is_displayed(), "Поле Email не подсвечено красным"
    # Проверка сообщения 'Ошибка' под полем Email
    def test_email_error_message_displayed_on_existing_user(self, driver):
        register_existing_user(driver)
        error_message = (WebDriverWait(driver, 10).
            until(expected_conditions.presence_of_element_located
            (TestLocators.EMAIL_ERROR)))
        assert error_message.is_displayed(), f"Ошибка не отображается. Текст: '{error_message.text}'"
    # Проверка красной подсветки для поля Пароль
    def test_password_field_highlighted_on_existing_user(self, driver):
        register_existing_user(driver)
        password_field =(WebDriverWait(driver, 3).
            until(expected_conditions.presence_of_element_located
            (TestLocators.PASSWORD_RED_FIELD)))
        assert password_field.is_displayed(), "Поле Пароль не подсвечено красным"
    # Проверка красной подсветки для поля Повторите Пароль
    def test_repeat_password_field_highlighted_on_existing_user(self, driver):
        register_existing_user(driver)
        submit_password_field = (WebDriverWait(driver, 3).
            until(expected_conditions.presence_of_element_located
            (TestLocators.SUBMIT_RED_FIELD)))
        assert  submit_password_field.is_displayed(), "Поле 'Повторите Пароль' не подсвечено красным"

